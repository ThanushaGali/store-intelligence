import json

with open(
    "data/output/events.json",
    "r"
) as f:
    events = json.load(f)

with open(
    "data/output/events.jsonl",
    "w"
) as f:

    for event in events:

        f.write(
            json.dumps(event)
            + "\n"
        )

print("events.jsonl created")