from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from fastapi import UploadFile, File, Form
import shutil
from fastapi.responses import FileResponse
from backend.services.pipeline import run_pipeline
from datetime import datetime


app = FastAPI(title="Store Intelligence API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EVENT_FILE = os.path.join(
    BASE_DIR,
    "data",
    "output",
    "events.json"
)



@app.get("/")
def home():
    return {
        "message": "Store Intelligence System Running"
    }


@app.get("/api/kpis")
def get_kpis():

    with open("data/output/kpis.json", "r") as f:
        data = json.load(f)

    return data

@app.get("/api/events")
def get_events():

    with open(EVENT_FILE, "r") as f:
        events = json.load(f)

    return events

@app.get("/api/footfall")
def footfall():

    with open(EVENT_FILE, "r") as f:
        events = json.load(f)

    entries = sum(
        1 for e in events
        if e["event_type"] == "ENTRY"
    )

    exits = sum(
        1 for e in events
        if e["event_type"] == "EXIT"
    )

    return {
        "entries": entries,
        "exits": exits,
        "occupancy": entries - exits
    }

@app.get("/api/top-brands")
def top_brands():

    import pandas as pd

    sales_file = os.path.join(
        BASE_DIR,
        "data",
        "sales",
        "sales_data.csv"
    )

    df = pd.read_csv(sales_file)

    brands = (
        df.groupby("brand_name")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    return brands.to_dict()

@app.get("/api/store-summary")
def store_summary():

    import pandas as pd

    sales_file = os.path.join(
        BASE_DIR,
        "data",
        "sales",
        "sales_data.csv"
    )

    with open(EVENT_FILE, "r") as f:
        events = json.load(f)

    df = pd.read_csv(sales_file)

    entries = sum(
        1 for e in events
        if e["event_type"] == "ENTRY"
    )

    exits = sum(
        1 for e in events
        if e["event_type"] == "EXIT"
    )

    occupancy = entries - exits

    total_revenue = float(
        df["total_amount"].sum()
    )

    top_brand = (
        df.groupby("brand_name")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )

    total_transactions = int(
        df["invoice_number"].nunique()
    )

    return {
        "footfall": entries,
        "occupancy": occupancy,
        "revenue": round(total_revenue, 2),
        "top_brand": top_brand,
        "transactions": total_transactions
    }

@app.get("/api/revenue")
def revenue():

    import pandas as pd

    sales_file = os.path.join(
        BASE_DIR,
        "data",
        "sales",
        "sales_data.csv"
    )

    df = pd.read_csv(sales_file)

    revenue = df["total_amount"].sum()

    transactions = df["invoice_number"].nunique()

    average_bill = revenue / transactions

    return {
        "total_revenue": float(revenue),
        "average_bill": round(average_bill, 2),
        "total_items_sold": int(df["qty"].sum())
    }

@app.get("/api/anomalies")
def anomalies():

    import pandas as pd

    sales_file = os.path.join(
        BASE_DIR,
        "data",
        "sales",
        "sales_data.csv"
    )

    df = pd.read_csv(sales_file)

    revenue = df["total_amount"].sum()

    transactions = df["order_id"].nunique()

    avg_bill = revenue / transactions

    with open("data/output/kpis.json", "r") as f:
        kpi_data = json.load(f)

    anomalies = kpi_data["anomalies"]

    return {
        "average_bill": round(avg_bill, 2),
        "anomalies": anomalies
    }

    
@app.get("/api/revenue-by-brand")
def revenue_by_brand():

    import pandas as pd

    sales_file = os.path.join(
        BASE_DIR,
        "data",
        "sales",
        "sales_data.csv"
    )

    df = pd.read_csv(sales_file)

    revenue = (
        df.groupby("brand_name")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    return revenue.to_dict()

@app.get("/api/zones")
def zones():

    zone_file = os.path.join(
        BASE_DIR,
        "data",
        "output",
        "zones.json"
    )

    with open("data/output/zones.json", "r") as f:
        data = json.load(f)

    return data

@app.get("/api/customer-journeys")
def customer_journey():

    with open(
        "data/output/customer_journey.json",
        "r"
    ) as f:

        data = json.load(f)

    return data

@app.get("/api/heatmap")
def heatmap():

    return FileResponse(
        "data/output/store_heatmap.jpg",
        media_type="image/jpeg"
    )

@app.get("/api/top-zone")
def top_zone():

    with open(
        "data/output/zones.json",
        "r"
    ) as f:

        zones = json.load(f)

    top = max(
        zones,
        key=zones.get
    )

    return {
        "zone": top,
        "visits": zones[top]
    }
@app.get("/api/journey-summary")
def journey_summary():

    with open(
        "data/output/customer_journey.json",
        "r"
    ) as f:

        journeys = json.load(f)

    return {
        "customers_tracked": len(journeys)
    }

@app.post("/upload-video")
async def upload_video(
    video: UploadFile = File(...),
    camera_type: str = Form(...)
):

    upload_path = f"data/uploads/{video.filename}"

    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    run_pipeline(
    upload_path,
    camera_type
)



@app.get("/api/recent-events")
def recent_events():

    with open(
        "data/output/events.json",
        "r"
    ) as f:
        events = json.load(f)

    return events[-20:]


    return {
        "message": "Analysis completed successfully",
        "status": "success"
    }

    from datetime import datetime
import os

@app.get("/health")
def health():

    kpi_file = "data/output/kpis.json"

    last_update = None

    if os.path.exists(kpi_file):
        last_update = datetime.fromtimestamp(
            os.path.getmtime(kpi_file)
        ).isoformat()

    return {
        "status": "healthy",
        "service": "Store Intelligence API",
        "last_update": last_update
    }

    
@app.get("/funnel")
def get_funnel():
    with open(
        "data/output/funnel.json",
        "r"
    ) as f:
        return json.load(f)

@app.get("/api/billing")
def get_billing():

    with open(
        "data/output/billing.json",
        "r"
    ) as f:

        return json.load(f)

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logging.info(
    "Analysis completed successfully"
)




