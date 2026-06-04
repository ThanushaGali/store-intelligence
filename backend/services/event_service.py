import json
from datetime import datetime

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

EVENT_FILE = os.path.join(
    BASE_DIR,
    "data",
    "output",
    "events.json"
)


def save_event(event_type, track_id, camera):

    event = {
        "event_type": event_type,
        "track_id": track_id,
        "camera": camera,
        "timestamp": datetime.now().isoformat()
    }

    with open(EVENT_FILE, "r") as f:
        events = json.load(f)

    events.append(event)

    with open(EVENT_FILE, "w") as f:
        json.dump(events, f, indent=4)

    print("Saved:", event)