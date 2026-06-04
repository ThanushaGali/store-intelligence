import pandas as pd

df = pd.read_csv("data/sales/sales_data.csv")

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumns:")
print(df.columns.tolist())

print("\nShape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())