# Store Intelligence System

## Overview

Store Intelligence System is an AI-powered retail analytics platform that converts CCTV footage and sales data into actionable business insights.

The system performs:

* Customer detection and tracking
* Footfall counting
* Entry/Exit event generation
* Zone analytics
* Customer journey analysis
* Billing analytics
* Conversion funnel generation
* Revenue analytics
* Heatmap generation
* Anomaly detection
* Interactive dashboard visualization

---

## Features

### Computer Vision Analytics

* YOLOv8-based person detection
* Multi-object tracking
* Entry and Exit detection
* Zone visit tracking
* Customer journey reconstruction

### Business Analytics

* Footfall analytics
* Occupancy tracking
* Revenue analytics
* Revenue per visitor
* Average bill value
* Conversion rate
* Top-performing brands
* Most visited zones

### Visualization

* KPI Dashboard
* Revenue by Brand chart
* Zone Analytics chart
* Customer Journey viewer
* Customer Funnel
* Heatmap visualization
* Anomaly alerts

### API Services

* FastAPI backend
* REST endpoints
* Health monitoring endpoint
* JSON analytics responses

---

# Project Structure

```text
store-intelligence/
│
├── analytics/
│   ├── entry_exit/
│   ├── zones/
│   ├── billing/
│   ├── heatmap/
│   ├── funnel/
│   ├── anomalies/
│   └── metrics/
│
├── backend/
│   └── main.py
│
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── style.css
│
├── data/
│   ├── Store 1/
│   ├── Store 2/
│   ├── layouts/
│   ├── sales/
│   └── output/
│
├── README.md
├── DESIGN.md
└── CHOICES.md
```

---

# Architecture

```text
Store CCTV Videos
        |
        v
YOLOv8 Detection
        |
        v
Object Tracking
        |
        v
Event Generation
        |
        +------------------+
        |                  |
        v                  v
Zone Analytics     Billing Analytics
        |                  |
        +--------+---------+
                 |
                 v
         Analytics Engine
                 |
                 v
           FastAPI Backend
                 |
                 v
        Interactive Dashboard
```

---

# Generated Outputs

The system generates:

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

---

# API Endpoints

### Health Check

```http
GET /health
```

### Store Summary

```http
GET /api/store-summary
```

### Revenue

```http
GET /api/revenue
```

### Revenue By Brand

```http
GET /api/revenue-by-brand
```

### Zone Analytics

```http
GET /api/zones
```

### Customer Journeys

```http
GET /api/customer-journeys
```

### KPIs

```http
GET /api/kpis
```

### Anomalies

```http
GET /api/anomalies
```

### Funnel Analytics

```http
GET /funnel
```

---

# Installation

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

Windows:

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Analytics

## Entry / Exit Analytics

```bash
python analytics/entry_exit/entry_exit_counter.py
```

## Zone Analytics

```bash
python analytics/zones/zone_tracker.py
```

## Billing Analytics

```bash
python analytics/billing/billing_counter.py
```

## Revenue Analytics

```bash
python analytics/revenue/revenue_tracker.py
```

## KPI Generation

```bash
python analytics/metrics/kpi_engine.py
```

## Funnel Generation

```bash
python analytics/funnel/funnel_generator.py
```

## Anomaly Detection

```bash
python analytics/anomalies/anomaly_detector.py
```

## Heatmap Generation

```bash
python analytics/heatmap/heatmap_generator.py store1
```

---

# Running Backend

```bash
cd backend

uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Running Frontend

Open:

```text
frontend/index.html
```

or run:

```bash
python -m http.server 5500
```

Dashboard:

```text
http://127.0.0.1:5500/frontend/index.html
```

---

# Health Endpoint Example

```json
{
  "status": "healthy",
  "service": "Store Intelligence API"
}
```

---

# AI-Assisted Development

AI tools were used for:

* Architecture brainstorming
* Analytics design discussions
* API design suggestions
* Dashboard improvements
* Documentation drafting
* Debugging assistance

Implementation, integration, testing, and validation were performed manually.

---

# Future Improvements

* Staff exclusion
* Re-identification models
* Multi-camera tracking
* Kafka streaming
* PostgreSQL storage
* ClickHouse analytics warehouse
* Redis caching
* WebSocket dashboard updates
* Deep learning anomaly detection

---

# Author

Thanusha Gali

