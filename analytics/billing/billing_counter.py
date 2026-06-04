from ultralytics import YOLO
import cv2
import json
import sys

model = YOLO("yolov8n.pt")

video_path = sys.argv[1]
print("Video:", video_path)

cap = cv2.VideoCapture(video_path)
print("Opened:", cap.isOpened())

billing_ids = set()

while cap.isOpened():
    print("Reading frame...")
    success, frame = cap.read()

    if not success:
        break

    results = model.track(
        frame,
        persist=True,
        classes=[0]
    )

    print("Boxes:", len(results[0].boxes))

    annotated = frame.copy()

    if results[0].boxes.id is not None:

        boxes = results[0].boxes

        for box in boxes:

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            track_id = int(
                box.id[0]
            )

            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            print(
    "ID:",
    track_id,
    "Center:",
    cx,
    cy
)


            cv2.circle(
                annotated,
                (cx, cy),
                5,
                (0, 0, 255),
                -1
            )

            # STORE BILLING ZONE
            if (
                400 < cx < 900
                and
                250 < cy < 900
            ):

                billing_ids.add(
                    track_id
                )

                cv2.rectangle(
                    annotated,
                    (400, 250),
                    (900, 900),
                    (0, 255, 0),
                    3
                )

    cv2.imshow(
        "Billing Counter",
        annotated
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

output = {
    "billing": len(
        billing_ids
    )
}

with open(
    "data/output/billing.json",
    "w"
) as f:

    json.dump(
        output,
        f,
        indent=4
    )

print("\nBilling Analytics")
print(output)

print(
    "billing.json saved successfully"
)