from ultralytics import YOLO
import cv2
from datetime import datetime
import os
import sys

import sys
import os

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

sys.path.append(ROOT_DIR)

from backend.services.event_service import save_event

model = YOLO("yolov8n.pt")

video_path = sys.argv[1]

cap = cv2.VideoCapture(video_path)

LINE_Y = 350

track_history = {}

counted_entries = set()
counted_exits = set()

entry_count = 0
exit_count = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    results = model.track(
        frame,
        persist=True,
        classes=[0],
        verbose=False
    )

    if results[0].boxes.id is not None:

        boxes = results[0].boxes.xyxy.cpu().numpy()
        ids = results[0].boxes.id.cpu().numpy()

        for box, track_id in zip(boxes, ids):
            x1, y1, x2, y2 = box
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)
            track_id = int(track_id)
            if track_id in track_history:
                prev_y = track_history[track_id]

                # ENTRY
                if (
                    prev_y < LINE_Y
                    and center_y >= LINE_Y
                    and track_id not in counted_entries
                ):
                    counted_entries.add(track_id)
                    entry_count += 1
                    save_event(
                        "ENTRY",
                        track_id,
                        "CAM3"
                    )

                    print({
                        "event": "ENTRY",
                        "track_id": track_id,
                        "time": str(datetime.now())
                    })

                # EXIT
                elif (
                    prev_y > LINE_Y
                    and center_y <= LINE_Y
                    and track_id not in counted_exits
                ):
                    counted_exits.add(track_id)
                    exit_count += 1
                    save_event(
                        "EXIT",
                        track_id,
                        "CAM3"
                    )

                    print({
                        "event": "EXIT",
                        "track_id": track_id,
                        "time": str(datetime.now())
                    })

            track_history[track_id] = center_y

            cv2.rectangle(
                frame,
                (int(x1), int(y1)),
                (int(x2), int(y2)),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"ID {track_id}",
                (int(x1), int(y1) - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    cv2.line(
    frame,
    (0, LINE_Y),
    (1920, LINE_Y),
    (0,0,255),
    3
)

    cv2.putText(
        frame,
        f"Entries: {entry_count}",
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Exits: {exit_count}",
        (50, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.imshow("Entry Exit Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("\nFinal Counts")
print("Entries:", entry_count)
print("Exits:", exit_count)