import pandas as pd

df = pd.read_csv("../data/raw/customer_support_tickets.csv")

print("=" * 50)
print("Dataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nMissing Values")
print(df.isnull().sum())

print("\nSample Records")
print(df.head())

print("\nCategory Distribution")
print(df["Ticket Type"].value_counts())