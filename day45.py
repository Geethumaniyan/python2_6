# ==========================================
# AI/ML Internship - Day 44
# Module 6: Introduction to YOLO & Computer Vision
# ==========================================

# ---------- THEORY ANSWERS ----------

print("\n1. What is Computer Vision?")
print("Computer Vision is a branch of Artificial Intelligence that enables computers to understand, analyze, and interpret images and videos.")

print("\n2. What is Object Detection?")
print("Object Detection identifies objects and their locations in an image.")

print("\n3. What is YOLO?")
print("YOLO (You Only Look Once) is a real-time object detection algorithm used in Computer Vision.")

print("\n4. What is a Bounding Box?")
print("A Bounding Box is a rectangle drawn around an object to show its location.")

print("\n5. Advantages of YOLO")
print("- Very Fast")
print("- Real-Time Detection")
print("- High Accuracy")
print("- Detects Multiple Objects")
print("- Easy Deployment")

# ---------- TASK 2 & TASK 3 ----------

from ultralytics import YOLO

print("\nYOLO imported successfully!")

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

print("YOLOv8 model loaded successfully!")

# ---------- TASK 4 ----------

print("\nYOLOv3")
print("- Released in 2018")
print("- Good speed and accuracy")
print("- Uses Darknet-53 architecture")

print("\nYOLOv5")
print("- Faster and easier to use")
print("- Developed by Ultralytics")
print("- Popular for custom object detection projects")

print("\nYOLOv8")
print("- Better accuracy and speed")
print("- Supports detection, segmentation, and classification")
print("- Easy deployment and training")

# ---------- TASK 5 ----------

print("\n10 Real-World Applications of YOLO")

applications = [
    "Self-Driving Cars",
    "Traffic Monitoring",
    "Face Detection",
    "CCTV Surveillance",
    "Intruder Detection",
    "Medical Imaging",
    "Retail Product Detection",
    "Customer Tracking",
    "Manufacturing Defect Detection",
    "Smart Security Systems"
]

for i, app in enumerate(applications, start=1):
    print(f"{i}. {app}")

# ---------- OBJECT DETECTION EXAMPLE ----------

# Uncomment the below lines if you have an image named image.jpg
#
# results = model("image.jpg")
# results[0].show()

print("\nDay 44 Assignment Completed Successfully!")