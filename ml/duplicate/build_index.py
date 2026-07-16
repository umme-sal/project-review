import faiss
import numpy as np
import pandas as pd

from sentence_transformers import SentenceTransformer

print("Loading dataset...")

df = pd.read_csv("../data/processed/cleaned_tickets.csv")

texts = df["text"].tolist()

print("Loading Sentence Transformer...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Generating embeddings...")

embeddings = model.encode(
    texts,
    show_progress_bar=True
)

embeddings = np.array(
    embeddings,
    dtype="float32"
)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(
    embeddings
)

faiss.write_index(
    index,
    "../models/faiss.index"
)

np.save(
    "../models/ticket_embeddings.npy",
    embeddings
)

df.to_csv(
    "../models/tickets.csv",
    index=False
)

print("Index Created Successfully")