import cv2
import os

video_folder = "data/videos"

for file in os.listdir(video_folder):

    if file.endswith(".mp4"):

        path = os.path.join(video_folder, file)

        cap = cv2.VideoCapture(path)

        fps = cap.get(cv2.CAP_PROP_FPS)

        frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

        duration = frames / fps

        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        print("\nVideo:", file)
        print("Resolution:", int(width), "x", int(height))
        print("FPS:", fps)
        print("Frames:", int(frames))
        print("Duration:", round(duration, 2), "seconds")

        cap.release()