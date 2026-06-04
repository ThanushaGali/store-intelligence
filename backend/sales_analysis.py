import pandas as pd

df = pd.read_csv("data/sales/sales_data.csv")

print("\nTop Brands")

print(
    df.groupby("brand_name")["qty"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nRevenue By Brand")

print(
    df.groupby("brand_name")["total_amount"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)