import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("../data/processed/cleaned_tickets.csv")

encoder = LabelEncoder()

df["label"] = encoder.fit_transform(df["category"])

df.to_csv(

    "../data/processed/training_dataset.csv",

    index=False

)

print(encoder.classes_)