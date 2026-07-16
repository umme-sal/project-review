import pandas as pd
import re


def clean_text(text):

    text = str(text).lower()

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"[^a-zA-Z0-9 ]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


df = pd.read_csv("../data/raw/customer_support_tickets.csv")

# Keep only required columns
df = df[["Ticket Description", "Ticket Type", "Ticket Priority"]]

# Rename columns
df.columns = [
    "text",
    "category",
    "priority"
]

# Remove missing values
df.dropna(inplace=True)

# Clean text
df["text"] = df["text"].apply(clean_text)

# Remove duplicates
df.drop_duplicates(inplace=True)

print(df.head())

print(df.shape)

df.to_csv(
    "../data/processed/cleaned_tickets.csv",
    index=False
)