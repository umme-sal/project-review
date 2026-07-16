from pathlib import Path

import faiss
import pandas as pd

from sentence_transformers import SentenceTransformer

MODEL_DIR = (
    Path(__file__).resolve().parent.parent
    / "models"
)


class DuplicateDetector:

    def __init__(self):

        print(f"Loading FAISS index from: {MODEL_DIR}")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.index = faiss.read_index(
            str(MODEL_DIR / "faiss.index")
        )

        self.df = pd.read_csv(
            MODEL_DIR / "tickets.csv"
        )

    def search(self, text, k=5):

        embedding = self.model.encode(
            [text]
        ).astype("float32")

        distance, indices = self.index.search(
            embedding,
            k
        )

        results = []

        for d, i in zip(distance[0], indices[0]):

            results.append({

                "ticket": self.df.iloc[i]["text"],

                "distance": float(d)

            })

        return results


detector = DuplicateDetector()