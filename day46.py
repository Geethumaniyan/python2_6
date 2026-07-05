"""
====================================================
AI/ML Internship - Day 46
Module 6: Understanding YOLO Detection Results
Complete Practical + Theory Answers
====================================================
"""

from ultralytics import YOLO

# ======================================
# Load YOLOv8 Model
# ======================================

model = YOLO("yolov8n.pt")

# ======================================
# Practical Task 1
# Run object detection on an image
# ======================================

results = model.predict(
    source="image.jpg",   # Replace with your image name
    conf=0.5,
    save=True
)

print("\n====================================")
print("OBJECT DETECTION RESULTS")
print("====================================\n")

# ======================================
# Practical Task 2
# Display detected objects and confidence
# ======================================

for result in results:

    print("Available Classes:")
    print(result.names)
    print()

    # ==================================
    # Practical Task 4
    # Print result.boxes
    # ==================================

    print("Bounding Box Information:")
    print(result.boxes)
    print()

    # ==================================
    # Practical Task 5
    # Print Class, Confidence and Bounding Box
    # ==================================

    for box in result.boxes:

        class_id = int(box.cls)

        class_name = result.names[class_id]

        confidence = float(box.conf)

        bounding_box = box.xyxy.tolist()[0]

        print("--------------------------------")
        print("Detected Object :", class_name)
        print("Confidence Score:", round(confidence, 2))
        print("Bounding Box    :", bounding_box)

print("\n====================================")
print("Practical Task 3")
print("Confidence Threshold Experiment")
print("====================================")

print("\nRunning with conf = 0.3")
model.predict("image.jpg", conf=0.3)

print("Completed")

print("\nRunning with conf = 0.5")
model.predict("image.jpg", conf=0.5)

print("Completed")

print("\nRunning with conf = 0.8")
model.predict("image.jpg", conf=0.8)

print("Completed")

# =====================================================
# THEORY ANSWERS
# =====================================================

print("\n")
print("=========================================")
print("THEORY ANSWERS")
print("=========================================\n")

print("1. What is a Class?")
print("Answer:")
print("A class is the category or label assigned to a detected object. Examples include Person, Car, Dog, Bus and Bicycle.\n")

print("2. What is a Bounding Box?")
print("Answer:")
print("A bounding box is a rectangle drawn around a detected object to show its exact location in an image.\n")

print("3. What is Confidence Score?")
print("Answer:")
print("Confidence score indicates how confident YOLO is that the detected object belongs to a particular class. Higher confidence means a more reliable prediction.\n")

print("4. What is Confidence Threshold?")
print("Answer:")
print("Confidence threshold is the minimum confidence score required for YOLO to display a detected object. Objects below this value are ignored.\n")

print("5. Why are Bounding Boxes Important?")
print("Answer:")
print("Bounding boxes help identify the exact location of objects in an image. They make it easier to visualize detected objects and are useful for tracking, counting, and analyzing them.\n")

# =====================================================
# SAMPLE OUTPUT
# =====================================================

print("=========================================")
print("SAMPLE OUTPUT")
print("=========================================\n")

print("Detected Object : person")
print("Confidence Score: 0.96")
print("Bounding Box    : [120.5, 60.3, 320.7, 450.9]")

print()

print("Detected Object : car")
print("Confidence Score: 0.91")
print("Bounding Box    : [420.8, 210.2, 760.1, 500.5]")

print()

print("Detected Object : dog")
print("Confidence Score: 0.93")
print("Bounding Box    : [60.1, 300.4, 250.8, 520.2]")

print("\n=========================================")
print("Day 46 Completed Successfully")
print("=========================================")