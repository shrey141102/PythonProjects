## Simple Python Screen Recorder

This is a simple Python script that can record your screen to a video file. 


**Requirements:**

* Python 3
* OpenCV ```pip install opencv-python```
* NumPy ```pip install numpy```
* PyAutoGUI ```pip install pyautogui```

**How to use:**

1. Run the [record.py](record.py)
2. Enter a filename (without extension).
3. It will record your screen for 5 seconds by default. You can change this by modifying the `recording_duration`.
4. The recorded video will be saved as `filename_YYYY-MM-DD_HH-MM-SS.mp4`.
