import pandas as pd
import json

sales_df = pd.read_csv(
    "data/sales/sales_data.csv"
)

revenue = sales_df["total_amount"].sum()

transactions = sales_df[
    "invoice_number"
].nunique()

if transactions > 0:
    average_bill = revenue / transactions
else:
    average_bill = 0

output = {
    "revenue": round(revenue, 2),
    "transactions": int(transactions),
    "average_bill": round(average_bill, 2)
}

with open(
    "data/output/revenue.json",
    "w"
) as f:

    json.dump(
        output,
        f,
        indent=4
    )

print("\nRevenue Analytics")
print(output)

print(
    "revenue.json saved successfully"
)