# Store Intelligence System

## AI-Powered Retail Analytics Platform

Store Intelligence System is an AI-powered retail analytics platform that transforms CCTV footage and sales data into actionable business intelligence.

The system leverages Computer Vision, Object Tracking, and Retail Analytics to automatically analyze customer movement inside stores and generate insights that help improve operational efficiency, customer engagement, and business performance.

By combining YOLOv8-based detection with analytics pipelines, the platform provides visibility into customer behavior, store traffic, zone performance, conversion funnels, revenue metrics, and heatmap visualizations.

---

## Overview

The platform processes store surveillance footage and transactional data to generate meaningful retail insights such as:

* Customer Detection & Tracking
* Footfall Analysis
* Entry & Exit Monitoring
* Zone Analytics
* Customer Journey Reconstruction
* Heatmap Generation
* Revenue Analytics
* Conversion Funnel Analytics
* KPI Generation
* Anomaly Detection

The objective is to bridge the gap between physical retail operations and data-driven decision making through Artificial Intelligence.

---

## Features

### Computer Vision Analytics

* YOLOv8-based person detection
* Multi-object tracking
* Entry and exit event generation
* Customer footfall counting
* Customer journey reconstruction
* Zone-wise visitor analytics
* Heatmap generation

### Business Intelligence

* Revenue analytics
* Revenue per visitor
* Average bill value
* Conversion rate analysis
* Brand-wise performance tracking
* KPI dashboard generation
* Business anomaly detection

### Interactive Dashboard

* Store Summary
* KPI Metrics
* Revenue Analysis
* Zone Analytics
* Customer Journey Visualization
* Conversion Funnel Analytics
* Heatmap Visualization
* Anomaly Reports

---

## Technology Stack

### Artificial Intelligence

* YOLOv8
* Computer Vision
* Object Tracking

### Backend

* Python
* FastAPI
* Pandas
* NumPy

### Frontend

* HTML
* CSS
* JavaScript

### Data Processing

* JSON
* CSV

### Containerization

* Docker
* Docker Compose

---

## System Architecture

```text
Store CCTV Videos
        │
        ▼
YOLOv8 Detection
        │
        ▼
Object Tracking
        │
        ▼
Event Generation
        │
 ┌──────┼─────────┐
 │      │         │
 ▼      ▼         ▼
Entry  Zones   Customer
Exit Analytics Journey Analytics
 │      │         │
 └──────┼─────────┘
        ▼
 Analytics Engine
        │
        ▼
 FastAPI Backend
        │
        ▼
 Interactive Dashboard
```

---

## Project Structure

```text
store-intelligence/

├── analytics/
├── backend/
├── detection/
├── frontend/
├── data/
├── README.md
├── DESIGN.md
├── CHOICES.md
├── Dockerfile
└── docker-compose.yml
```

---

## Quick Start

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Backend

```bash
cd backend
uvicorn main:app --reload
```

### Open Dashboard

```text
http://127.0.0.1:8000/docs
```


## Future Improvements

* Multi-camera tracking
* Customer re-identification
* Real-time analytics pipeline
* PostgreSQL integration
* ClickHouse analytics warehouse
* Kafka streaming architecture
* Redis caching layer
* WebSocket-based live dashboard updates
* Predictive customer analytics
* AI-driven demand forecasting
* Deep learning anomaly detection
* Store layout optimization recommendations




---


## Project Resources

### Project Presentation

A detailed project presentation is available in the `docs/` directory, covering:

- Problem Statement
- Solution Design
- System Architecture
- Analytics Pipeline
- Implementation Approach
- Key Features
- Future Scope

### Demonstration Assets

The `assets/` directory contains sample screenshots and outputs generated during development and testing, including:

- Customer Tracking
- Entry & Exit Detection
- Zone Analytics
- Dashboard Visualizations


These resources are provided to help understand the system workflow and demonstrate the capabilities of the platform.

---



## License

This project is licensed under the MIT License.

See the LICENSE file for more information.

---

## Author

**Thanusha Gali**


