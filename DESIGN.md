# Store Intelligence System - Design Document

## Overview

The Store Intelligence System is an AI-powered retail analytics platform that transforms CCTV footage and sales data into actionable business intelligence. The system combines computer vision, multi-object tracking, event generation, analytics processing, REST APIs, and an interactive dashboard.

The objective is to automatically measure customer behavior, store performance, zone engagement, billing activity, customer journeys, conversion funnels, and revenue insights from retail store surveillance footage.

---

# System Architecture

```text
Store CCTV Videos
        |
        v
YOLOv8 Person Detection
        |
        v
Multi-Object Tracking
        |
        v
Event Generation
(ENTRY / EXIT)
        |
        +----------------+
        |                |
        v                v
 Zone Tracking      Billing Analytics
        |                |
        +--------+-------+
                 |
                 v
          Analytics Engine
                 |
    +------------+-------------+
    |            |             |
    v            v             v
 KPI Engine  Funnel Engine  Anomaly Engine
                 |
                 v
          FastAPI Backend
                 |
                 v
        Interactive Dashboard
```

---

# Component Design

## 1. Detection Layer

The system uses YOLOv8 for customer detection from CCTV footage.

Responsibilities:

* Detect customers from video frames
* Ignore non-human objects
* Generate bounding boxes
* Feed detections into tracking pipeline

Output:

```json
{
  "track_id": 12,
  "bbox": [x1, y1, x2, y2]
}
```

---

## 2. Tracking Layer

Multi-object tracking maintains customer identities across frames.

Responsibilities:

* Assign persistent track IDs
* Handle temporary occlusions
* Reduce duplicate counting
* Support customer re-entry tracking

Output:

```json
{
  "track_id": 12,
  "center_x": 1050,
  "center_y": 450
}
```

---

## 3. Event Generation Layer

A virtual counting line is placed near store entry and exit points.

Generated events:

* ENTRY
* EXIT

Example:

```json
{
  "event_type": "ENTRY",
  "track_id": 12,
  "camera": "CAM3",
  "timestamp": "2026-06-03T18:49:24"
}
```

Events are stored in JSON and JSONL formats for downstream analytics.

---

## 4. Zone Analytics Engine

Customer positions are mapped to predefined store zones.

Example zones:

* Farm Stay
* The Face Shop
* Good Vibes
* Derma Co
* Minimalist
* Aqualogica

Generated Output:

```json
{
  "Farm Stay": 17,
  "The Face Shop": 17,
  "Good Vibes": 16,
  "Derma Co": 19,
  "Minimalist": 17,
  "Aqualogica": 0
}
```

The output is visualized in dashboard charts.

---

## 5. Customer Journey Engine

Customer movement is reconstructed using generated events and tracked zone visits.

Example:

```text
ENTRY
→ Farm Stay
→ Derma Co
→ Billing
→ EXIT
```

Customer journeys provide insights into navigation patterns and zone engagement.

---

## 6. Billing Analytics Engine

Billing-area CCTV footage is analyzed separately.

Responsibilities:

* Detect customers entering billing area
* Count billing interactions
* Measure checkout activity

Output:

```json
{
  "billing": 18
}
```

This metric is used for funnel generation and conversion analysis.

---

## 7. Funnel Analytics Engine

The funnel engine generates customer conversion stages.

Stages:

* Entry
* Zone Visit
* Billing
* Purchase

Example:

```json
{
  "entry": 18,
  "zone_visit": 15,
  "billing": 18,
  "purchase": 14
}
```

This provides store conversion insights.

---

## 8. KPI Engine

Business KPIs are generated using event data, billing data, and sales records.

Generated KPIs:

* Footfall
* Revenue
* Transactions
* Average Bill Value
* Conversion Rate
* Revenue Per Visitor
* Top Brand
* Most Visited Zone

Output:

```json
{
  "footfall": 18,
  "revenue": 34331.71,
  "transactions": 24
}
```

---

## 9. Heatmap Engine

Real customer coordinates are accumulated across frames.

Processing:

1. Track customer centers
2. Store coordinate points
3. Apply Gaussian Blur
4. Generate density visualization

Output:

```text
store_heatmap.jpg
```

The heatmap highlights:

* High traffic areas
* Low engagement areas
* Customer movement density

---

## 10. Anomaly Detection Engine

Rule-based anomaly detection identifies unusual store behavior.

Current checks:

* Low Revenue
* Low Transaction Volume
* Low Average Bill Value

Output:

```json
{
  "anomalies": []
}
```

---

# API Design

FastAPI exposes analytics through REST endpoints.

Endpoints:

```text
/health

/api/store-summary
/api/revenue
/api/revenue-by-brand
/api/zones
/api/customer-journeys
/api/kpis
/api/anomalies

/funnel
/upload-video
```

All endpoints return JSON responses.

---

# Dashboard Design

Frontend Technologies:

* HTML
* CSS
* JavaScript
* Chart.js

Dashboard Components:

* KPI Cards
* Revenue by Brand Chart
* Zone Analytics Chart
* Customer Journey Viewer
* Customer Funnel
* Store Heatmap
* Anomaly Indicators

The dashboard automatically refreshes and updates analytics.

---

# Data Storage

Generated artifacts:

```text
events.json
events.jsonl
zones.json
billing.json
customer_journey.json
funnel.json
kpis.json
anomalies.json
heat_points.json
store_heatmap.jpg
```

Current implementation uses local file storage for simplicity and portability.

---

# AI-Assisted Decisions

AI tools were used to:

* Design analytics architecture
* Improve KPI calculations
* Design dashboard components
* Generate API structures
* Improve anomaly detection logic
* Assist with debugging and code reviews

Final implementation decisions, testing, integration, and validation were performed manually.

---

# Future Improvements

* Multi-camera customer stitching
* Staff identification and exclusion
* Group customer detection
* Real-time stream processing
* Kafka integration
* PostgreSQL persistence
* ClickHouse analytics warehouse
* WebSocket live dashboard updates
* Deep learning anomaly detection

---

# Conclusion

The Store Intelligence System demonstrates a complete end-to-end retail analytics pipeline that transforms CCTV footage and sales data into actionable business intelligence through computer vision, event generation, analytics processing, APIs, and interactive dashboards.
