import cv2

video_path = "data/videos/cam3.mp4"

cap = cv2.VideoCapture(video_path)

ret, frame = cap.read()

if ret:

    cv2.line(
        frame,
        (1100, 0),
        (1100, 1080),
        (0, 255, 0),
        3
    )

    cv2.imwrite(
        "data/output/cam3_line.jpg",
        frame
    )

    print("Line image saved")

cap.release()