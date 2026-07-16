from pathlib import Path

import torch
from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification
)

# Absolute path to the trained model
MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "ticket_classifier"
)


class TicketClassifier:

    def __init__(self):

        # Select device
        if torch.cuda.is_available():
            self.device = torch.device("cuda")
        elif torch.backends.mps.is_available():
            self.device = torch.device("mps")
        else:
            self.device = torch.device("cpu")

        print(f"Loading model from: {MODEL_PATH}")
        print(f"Using device: {self.device}")

        # Load tokenizer
        self.tokenizer = DistilBertTokenizerFast.from_pretrained(
            str(MODEL_PATH)
        )

        # Load model
        self.model = DistilBertForSequenceClassification.from_pretrained(
            str(MODEL_PATH)
        )

        self.model.to(self.device)
        self.model.eval()

        self.labels = {
            0: "Billing inquiry",
            1: "Cancellation request",
            2: "Product inquiry",
            3: "Refund request",
            4: "Technical issue"
        }

    def predict(self, text: str):

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=128
        )

        inputs = {
            key: value.to(self.device)
            for key, value in inputs.items()
        }

        with torch.no_grad():
            outputs = self.model(**inputs)

        probabilities = torch.softmax(outputs.logits, dim=1)

        prediction = torch.argmax(probabilities, dim=1).item()

        confidence = probabilities[0][prediction].item()

        return {
            "category": self.labels[prediction],
            "confidence": round(confidence, 4)
        }


classifier = TicketClassifier()