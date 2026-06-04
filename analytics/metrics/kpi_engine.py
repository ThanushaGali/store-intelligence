import pandas as pd
import json

# Load Sales Data
sales_df = pd.read_csv("data/sales/sales_data.csv")

# Load Events
try:
    with open("data/output/events.json", "r") as f:
        events = json.load(f)
except:
    events = []

# Load Zones
try:
    with open("data/output/zones.json", "r") as f:
        zones = json.load(f)
except:
    zones = {}

# -------------------------
# FOOTFALL
# -------------------------

unique_visitors = set()

for event in events:

    if event["event_type"] == "ENTRY":

        unique_visitors.add(
            event["track_id"]
        )

footfall = len(unique_visitors)

# -------------------------
# REVENUE
# -------------------------

with open(
    "data/output/revenue.json",
    "r"
) as f:

    revenue_data = json.load(f)

revenue = revenue_data["revenue"]

transactions = revenue_data["transactions"]

average_bill = revenue_data["average_bill"]

# -------------------------
# TRANSACTIONS
# -------------------------

transactions = sales_df["invoice_number"].nunique()

# -------------------------
# AVERAGE BILL VALUE
# -------------------------

if transactions > 0:
    average_bill = revenue / transactions
else:
    average_bill = 0

# -------------------------
# CONVERSION RATE
# -------------------------

converted_customers = min(
    transactions,
    footfall
)

if footfall > 0:
    conversion_rate = round(
        (converted_customers / footfall) * 100,
        2
    )
else:
    conversion_rate = 0

# -------------------------
# REVENUE PER VISITOR
# -------------------------

if footfall > 0:
    revenue_per_visitor = revenue / footfall
else:
    revenue_per_visitor = 0

sales_per_transaction = 0

if transactions > 0:
    sales_per_transaction = revenue / transactions

# -------------------------
# TOP BRAND
# -------------------------

top_brand = (
    sales_df.groupby("brand_name")["qty"]
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

# -------------------------
# MOST VISITED ZONE
# -------------------------

most_visited_zone = max(zones, key=zones.get)

# -------------------------
# OUTPUT
# -------------------------

anomalies = []

if average_bill < 500:
    anomalies.append(
        "Low Average Bill Value"
    )

if conversion_rate < 80:
    anomalies.append(
        "Low Conversion Activity"
    )

kpis = {
    "footfall": footfall,
    "revenue": round(revenue, 2),
    "transactions": int(transactions),
    "average_bill": round(average_bill, 2),
    "conversion_rate": round(conversion_rate, 2),
    "revenue_per_visitor": round(revenue_per_visitor, 2),
    "top_brand": top_brand,
    "most_visited_zone": most_visited_zone,
    "sales_per_transaction":round(sales_per_transaction, 2),
    "anomalies": anomalies
}

print("\nSTORE KPIs\n")

for key, value in kpis.items():
    print(key, ":", value)

with open("data/output/kpis.json", "w") as f:
    json.dump(kpis, f, indent=4)

print("\nkpis.json saved successfully")