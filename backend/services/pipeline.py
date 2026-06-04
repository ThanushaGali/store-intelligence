import subprocess
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def run_pipeline(
    video_path,
    camera_type
):

    logging.info(
    "Starting pipeline..."
)
    print("Video:", video_path)
    print("Camera Type:", camera_type)

    # Entry Camera
    if camera_type == "entry":

        subprocess.run([
            "python",
            "detection/events/entry_exit_counter.py",
            video_path
        ])

    # Zone Camera
    elif camera_type == "zone":

        subprocess.run([
            "python",
            "analytics/zones/zone_analytics.py",
            video_path
        ])

    # Billing Camera (future use)
    elif camera_type == "billing":

        print("Billing analytics not implemented yet")

    # Common analytics
    subprocess.run([
        "python",
        "analytics/journey/customer_journey.py"
    ])

    subprocess.run([
        "python",
        "analytics/heatmap/heatmap_generator.py"
    ])

    subprocess.run([
        "python",
        "analytics/anomalies/anomaly_detector.py"
    ])

    subprocess.run([
        "python",
        "analytics/metrics/kpi_engine.py"
    ])

    subprocess.run([
    "python",
    "analytics/revenue/revenue_tracker.py"
])

    logging.info(
    "Pipeline completed"
)