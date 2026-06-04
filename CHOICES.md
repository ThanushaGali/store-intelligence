# Edge Cases and Handling

## Re-Entry Handling

A customer may exit and later re-enter the store.

Current Handling:

* Events are generated using tracked IDs.
* Duplicate counting within a continuous tracking session is reduced.
* Funnel analytics uses unique visitor counts.

Limitation:

* If a customer disappears for a long duration and receives a new tracking ID, they may be counted as a new visitor.

Future Improvement:

* Person re-identification (ReID) models can preserve identities across cameras and long gaps.

---

## Staff Exclusion

Store employees frequently move through the store and can artificially increase footfall metrics.

Current Handling:

* No dedicated employee classifier is currently implemented.

Limitation:

* Employees may be included in customer analytics.

Future Improvement:

* Uniform detection
* Badge recognition
* Re-identification profiles for staff exclusion

---

## Group Entry Handling

Customers entering together may partially overlap.

Current Handling:

* YOLOv8 detection combined with object tracking attempts to maintain separate identities.

Limitation:

* Heavy overlap can occasionally cause ID switches.

Future Improvement:

* StrongSORT or ByteTrack integration
* Multi-camera fusion

---

## Occlusion Handling

Customers may become partially hidden by shelves or other customers.

Current Handling:

* Tracker persistence helps preserve identities during short occlusions.

Limitation:

* Long occlusions may cause track loss.

Future Improvement:

* Re-identification models
* Multi-camera tracking

---

# Funnel Analytics Decisions

## Why Funnel Analytics?

Retail performance is better understood through customer progression rather than raw counts.

Implemented funnel stages:

```text
Entry
→ Zone Visit
→ Billing
→ Purchase
```

Benefits:

* Conversion measurement
* Checkout drop-off analysis
* Store performance monitoring

Trade-off:

The current implementation uses aggregated analytics and billing counts rather than complete per-customer checkout attribution.

---

# Billing Analytics Decisions

## Why Separate Billing Detection?

Billing counters represent the strongest indicator of purchase intent.

A dedicated billing video is processed separately to:

* Measure checkout engagement
* Improve funnel accuracy
* Support conversion analytics

Trade-off:

Requires an additional camera stream but produces richer business insights.

---

# Heatmap Design Decisions

## Why Real Coordinate Heatmaps?

Rather than using manually created hotspot zones, the system stores actual customer coordinates.

Processing Pipeline:

1. Collect tracked positions
2. Store coordinates
3. Apply Gaussian blur
4. Generate density visualization

Benefits:

* Real customer movement representation
* Better store layout analysis
* More accurate engagement visualization

---

# Structured Logging Decisions

FastAPI and analytics modules generate structured logs.

Example:

```text
INFO: GET /api/store-summary 200 OK
INFO: GET /api/kpis 200 OK
```

Benefits:

* Easier debugging
* Health monitoring
* Production readiness

---

# Health Endpoint Decision

A dedicated health endpoint was implemented.

Endpoint:

```text
/health
```

Response:

```json
{
  "status": "healthy",
  "service": "Store Intelligence API"
}
```

Benefits:

* Service monitoring
* Deployment validation
* Container health checks

---

# AI-Assisted Engineering Decisions

AI assistance was used during development for:

* Architecture brainstorming
* Analytics pipeline design
* Dashboard design improvements
* API design suggestions
* Debugging support
* Documentation drafting

Engineering decisions, implementation, integration, testing, and validation were performed manually.

---

# Conclusion

The Store Intelligence System prioritizes correctness, explainability, modularity, and reproducibility. Design decisions emphasize practical deployment, business value, and evaluation readiness while maintaining a clear upgrade path toward production-scale retail analytics systems.
