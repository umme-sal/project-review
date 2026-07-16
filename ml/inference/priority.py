from pathlib import Path
import torch
from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification
)

MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "priority_classifier"
)


class PriorityClassifier:

    def __init__(self):

        if torch.cuda.is_available():
            self.device = torch.device("cuda")
        elif torch.backends.mps.is_available():
            self.device = torch.device("mps")
        else:
            self.device = torch.device("cpu")

        self.tokenizer = DistilBertTokenizerFast.from_pretrained(
            str(MODEL_PATH)
        )

        self.model = DistilBertForSequenceClassification.from_pretrained(
            str(MODEL_PATH)
        )

        self.model.to(self.device)
        self.model.eval()

        self.labels = {
            0: "Critical",
            1: "High",
            2: "Low",
            3: "Medium"
        }

    def predict(self, text):

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=128
        )

        inputs = {
            k: v.to(self.device)
            for k, v in inputs.items()
        }

        with torch.no_grad():
            outputs = self.model(**inputs)

        probs = torch.softmax(outputs.logits, dim=1)

        pred = torch.argmax(probs, dim=1).item()

        return {
            "priority": self.labels[pred],
            "confidence": round(probs[0][pred].item(), 4)
        }


priority_classifier = PriorityClassifier()