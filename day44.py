# ==========================================
# AI/ML Internship – Day 44
# Module 6: Introduction to YOLO & Computer Vision
# ==========================================

# ------------------------------------------
# THEORY ANSWERS
# ------------------------------------------

# 1. What is Computer Vision?
# Computer Vision is a branch of Artificial Intelligence (AI)
# that enables computers to understand, analyze, and interpret
# images and videos.

# 2. What is Object Detection?
# Object Detection is a Computer Vision technique that identifies
# objects in an image and locates them using bounding boxes.

# 3. What is YOLO?
# YOLO (You Only Look Once) is a real-time object detection
# algorithm that can detect, classify, and locate objects in
# a single pass.

# 4. What is a Bounding Box?
# A Bounding Box is a rectangular box drawn around a detected
# object to show its location in an image.

# 5. Advantages of YOLO
# - Very Fast
# - Real-Time Detection
# - High Accuracy
# - Detects Multiple Objects
# - Easy Deployment


# ------------------------------------------
# PRACTICAL TASK 1
# Install YOLO
# ------------------------------------------

# Run this command in Terminal:
# pip install ultralytics


# ------------------------------------------
# PRACTICAL TASK 2
# Import YOLO
# ------------------------------------------

from ultralytics import YOLO


# ------------------------------------------
# PRACTICAL TASK 3
# Load YOLOv8 Model
# ------------------------------------------

model = YOLO("yolov8n.pt")

print("YOLOv8 model loaded successfully!")


# ------------------------------------------
# PRACTICAL TASK 4
# Research on YOLO Versions
# ------------------------------------------

yolo_versions = {
    "YOLOv3": "Introduced Darknet-53 backbone and improved detection accuracy.",
    "YOLOv5": "Popular version developed by Ultralytics, easy to train and deploy.",
    "YOLOv8": "Latest Ultralytics version with improved speed, accuracy, and usability."
}

print("\nYOLO Version Research:")
for version, description in yolo_versions.items():
    print(f"{version}: {description}")


# ------------------------------------------
# PRACTICAL TASK 5
# 10 Real-World Applications of YOLO
# ------------------------------------------

applications = [
    "1. Self-Driving Cars",
    "2. Face Detection and Recognition",
    "3. CCTV Surveillance",
    "4. Traffic Monitoring",
    "5. Medical Image Analysis",
    "6. Retail Product Detection",
    "7. Intruder Detection Systems",
    "8. Industrial Defect Detection",
    "9. Wildlife Monitoring",
    "10. Smart City Applications"
]

print("\n10 Real-World Applications of YOLO:")
for app in applications:
    print(app)


# ------------------------------------------
# Example Object Detection Code
# ------------------------------------------

# Uncomment the code below after placing an image
# in the same folder as this script.

"""
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("image.jpg")

results[0].show()

print("Object Detection Completed!")
"""