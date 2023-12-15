# importing the dependencies
import cv2
import numpy as np
import pyautogui
from datetime import datetime

# Get screen resolution
# to set resolution manually use resolution = (1920, 1080)

screen_width, screen_height = pyautogui.size()
resolution = (screen_width, screen_height)

filename = input("Enter filename (without extension): ")

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_filename = f"{filename}_{timestamp}.mp4"

fps = 30
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_filename, fourcc, fps, resolution)

recording_duration = 5 # seconds

# to record for more than a miniute uncomment the line below and comment the old one
# for _ in range(int(fps * recording_duration * 60)):
for _ in range(int(fps * recording_duration)):
    screen = pyautogui.screenshot()

    frame = np.array(screen)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    out.write(frame)

out.release()
print(f"Recording saved as '{output_filename}'.")

