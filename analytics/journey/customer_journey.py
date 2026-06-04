import json

with open(
    "data/output/events.json",
    "r"
) as f:
    events = json.load(f)

with open(
    "data/output/zones.json",
    "r"
) as f:
    zones = json.load(f)

top_zone = max(
    zones,
    key=zones.get
)

journeys = {}

for event in events:

    track_id = str(
        event["track_id"]
    )

    if track_id not in journeys:
        journeys[track_id] = []

    if event["event_type"] == "ENTRY":
        journeys[track_id].append(
            "ENTRY"
        )

    elif event["event_type"] == "EXIT":

        journeys[track_id].append(
            "EXIT"
        )

with open(
    "data/output/customer_journey.json",
    "w"
) as f:

    json.dump(
        journeys,
        f,
        indent=4
    )

print("Customer journeys saved")