import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

video_path = "data/videos/cam3.mp4"

cap = cv2.VideoCapture(video_path)

ret, frame = cap.read()

results = model(frame, conf=0.4)

annotated = results[0].plot()

cv2.imwrite(
    "data/output/cam3_detection.jpg",
    annotated
)

print("Detection image saved")

cap.release()