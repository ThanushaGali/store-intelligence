from ultralytics import YOLO
import cv2
import json
import sys

model = YOLO("yolov8n.pt")

video_path = sys.argv[1]

cap = cv2.VideoCapture(video_path)

heat_points = []

zone_counts = {
    "Farm Stay": set(),
    "The Face Shop": set(),
    "Good Vibes": set(),
    "Derma Co": set(),
    "Minimalist": set(),
    "Aqualogica": set()
}

while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    results = model.track(
        frame,
        persist=True,
        classes=[0]
    )

    annotated = frame.copy()

    if results[0].boxes.id is not None:

        boxes = results[0].boxes

        for box in boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            track_id = int(box.id[0])

            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            heat_points.append([cx, cy])

            # Person center point
            cv2.circle(
                annotated,
                (cx, cy),
                5,
                (0, 0, 255),
                -1
            )

            print("ID:", track_id, "Center:", cx, cy)

            # ---------- Lakme Zone ----------
            if cx < 250:
                zone_counts["Farm Stay"].add(track_id)
            elif cx < 650:
                zone_counts["The Face Shop"].add(track_id)
            elif cx < 950:
                zone_counts["Good Vibes"].add(track_id)
            elif cx < 1250:
                zone_counts["Derma Co"].add(track_id)
            elif cx < 1550:
                zone_counts["Minimalist"].add(track_id)
            else:
                zone_counts["Aqualogica"].add(track_id)

        

    # Draw Zones

    

    cv2.imshow("Zone Tracking", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

output = {
    zone: len(ids)
    for zone, ids in zone_counts.items()
}

print("\nFinal Zone Counts")
print(output)

with open(
    "data/output/zones.json",
    "w"
) as f:

    json.dump(
        output,
        f,
        indent=4
    )

with open(
    "data/output/heat_points.json",
    "w"
) as f:

    json.dump(
        heat_points,
        f
    )

print("heat_points.json saved")

print("zones.json saved successfully")