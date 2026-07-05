"""
=========================================================
 AI/ML Internship – Day 47
 Module 6: Detecting Objects in Videos Using YOLO &
 Real-Time Webcam Detection
=========================================================

-----------------------------
THEORY ANSWERS
-----------------------------

1. What is Video Object Detection?
Answer:
Video Object Detection is the process of detecting and locating objects in each frame of a video continuously.

2. What is Real-Time Detection?
Answer:
Real-Time Detection is detecting objects live using a webcam or camera.

3. What is OpenCV?
Answer:
OpenCV (Open Source Computer Vision Library) is an open-source library used for image processing, video processing, and computer vision applications.

4. Why is YOLO suitable for video detection?
Answer:
YOLO is fast, accurate, and capable of detecting multiple objects in real time.

5. What does VideoCapture(0) mean?
Answer:
cv2.VideoCapture(0) opens the default webcam connected to the computer.

-------------------------------------------------
PRACTICAL TASK 1
Install Required Libraries
-------------------------------------------------

Run these commands in VS Code Terminal:

pip install ultralytics
pip install opencv-python

-------------------------------------------------
PRACTICAL TASK 2
Load YOLO Model
-------------------------------------------------
"""

from ultralytics import YOLO
import cv2

# Load YOLO Model
model = YOLO("yolov8n.pt")

print("YOLO Model Loaded Successfully!")

"""
-------------------------------------------------
PRACTICAL TASK 3
Video Object Detection
-------------------------------------------------

Place a video named:

video.mp4

inside the same folder.

Uncomment the following code to run video detection.
"""

'''
video = cv2.VideoCapture("video.mp4")

while True:

    success, frame = video.read()

    if not success:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Video Detection", annotated_frame)

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()
'''

"""
-------------------------------------------------
PRACTICAL TASK 4
Real-Time Webcam Detection
-------------------------------------------------
"""

camera = cv2.VideoCapture(0)

print("Webcam Started...")
print("Show a Person, Laptop and Mobile Phone")
print("Press ESC to Exit")

while True:

    success, frame = camera.read()

    if not success:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Live Detection", annotated_frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()

-------------------------------------------------
#PRACTICAL TASK 5
#Detect:
✓ Person
✓ Mobile Phone
✓ Laptop

Show these objects to your webcam.

YOLO will display something like:

Person       96%
Laptop       94%
Cell Phone   91%

with bounding boxes.

-------------------------------------------------
EXPECTED FOLDER STRUCTURE
-------------------------------------------------

Day47/

│── day47_yolo_video_webcam.py
│── video.mp4
│── yolov8n.pt

-------------------------------------------------
VIVA QUESTIONS
-------------------------------------------------

Q1. What is Video Object Detection?
Answer:
Detecting objects in every frame of a video.

Q2. What is Real-Time Detection?
Answer:
Detecting objects live using a webcam.

Q3. What is OpenCV?
Answer:
An Open Source Computer Vision Library.

Q4. Why is YOLO suitable for video detection?
Answer:
Because it is fast and suitable for real-time object detection.

Q5. What does VideoCapture(0) mean?
Answer:
It opens the default webcam.

Q6. Which YOLO model is best for beginners?
Answer:
yolov8n.pt

Q7. Which key exits the program?
Answer:
ESC key.

Q8. Which function displays the output window?
Answer:
cv2.imshow()

Q9. Which function reads a frame?
Answer:
camera.read() or video.read()

Q10. Which library is used for computer vision?
Answer:
OpenCV (cv2)

======================
END OF DAY 47
======================