import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

import numpy as np
import pandas as pd

from datasets import Dataset

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
)

from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification,
    Trainer,
    TrainingArguments,
)

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

df = pd.read_csv("../data/processed/cleaned_tickets.csv")

# Encode Priority Labels
priority_map = {
    "Low": 0,
    "Medium": 1,
    "High": 2,
    "Critical": 3,
}

df = df[df["priority"].isin(priority_map.keys())]

df["label"] = df["priority"].map(priority_map)

# ---------------------------------------------------
# Train Test Split
# ---------------------------------------------------

train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42,
    stratify=df["label"],
)

train_dataset = Dataset.from_pandas(train_df)
test_dataset = Dataset.from_pandas(test_df)

# ---------------------------------------------------
# Tokenizer
# ---------------------------------------------------

tokenizer = DistilBertTokenizerFast.from_pretrained(
    "distilbert-base-uncased"
)


def tokenize(batch):
    return tokenizer(
        batch["text"],
        truncation=True,
        padding="max_length",
        max_length=128,
    )


train_dataset = train_dataset.map(tokenize, batched=True)
test_dataset = test_dataset.map(tokenize, batched=True)

train_dataset.set_format(
    "torch",
    columns=[
        "input_ids",
        "attention_mask",
        "label",
    ],
)

test_dataset.set_format(
    "torch",
    columns=[
        "input_ids",
        "attention_mask",
        "label",
    ],
)

# ---------------------------------------------------
# Model
# ---------------------------------------------------

model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=4,
)

# ---------------------------------------------------
# Metrics
# ---------------------------------------------------


def compute_metrics(pred):

    labels = pred.label_ids

    preds = np.argmax(
        pred.predictions,
        axis=1,
    )

    precision, recall, f1, _ = precision_recall_fscore_support(
        labels,
        preds,
        average="weighted",
    )

    accuracy = accuracy_score(
        labels,
        preds,
    )

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


# ---------------------------------------------------
# Training Arguments
# ---------------------------------------------------

training_args = TrainingArguments(
    output_dir="../models/priority_checkpoints",

    eval_strategy="epoch",
    save_strategy="epoch",

    learning_rate=2e-5,

    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,

    num_train_epochs=2,

    weight_decay=0.01,

    load_best_model_at_end=True,

    logging_dir="../logs",

    logging_steps=50,

    report_to="none",
)

# ---------------------------------------------------
# Trainer
# ---------------------------------------------------

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics,
)

# ---------------------------------------------------
# Train
# ---------------------------------------------------

trainer.train()

# ---------------------------------------------------
# Save Model
# ---------------------------------------------------

trainer.save_model(
    "../models/priority_classifier"
)

tokenizer.save_pretrained(
    "../models/priority_classifier"
)

print("\nPriority Model Saved Successfully!\n")