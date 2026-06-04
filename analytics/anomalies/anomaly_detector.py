import pandas as pd
import json

sales_file = "data/sales/sales_data.csv"

df = pd.read_csv(sales_file)

revenue = df["total_amount"].sum()

transactions = df["order_id"].nunique()

average_bill = revenue / transactions

anomalies = []

# Low Average Bill

if average_bill < 500:

    anomalies.append(
        "Low Average Bill Value"
    )

# Low Revenue

if revenue < 10000:

    anomalies.append(
        "Low Revenue"
    )

# Very Low Transactions

if transactions < 5:

    anomalies.append(
        "Low Transaction Volume"
    )

print("\nStore Analytics")

print("Revenue:", revenue)
print("Transactions:", transactions)
print("Average Bill:", round(average_bill, 2))

if anomalies:

    print("\nANOMALIES DETECTED")

    for anomaly in anomalies:

        print("-", anomaly)

else:

    print("\nNormal Store Performance")

with open(
    "data/output/anomalies.json",
    "w"
) as f:

    json.dump(
        {
            "anomalies": anomalies
        },
        f,
        indent=4
    )

print("\nanomalies.json saved")