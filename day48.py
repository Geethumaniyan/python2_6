# ============================================================
# AI/ML Internship – Day 48
# Module 6: Custom Object Detection – Training YOLO
# ============================================================


# ============================================================
# Practical Task 1
# Install YOLO
# ============================================================

# Run this command in the VS Code Terminal (NOT inside Python)

# pip install ultralytics


# ============================================================
# Practical Task 2
# Research on Annotation Tools
# ============================================================

print("\n========== Annotation Tools ==========\n")

print("1. LabelImg")
print("- Free and Open Source")
print("- Used for image annotation")
print("- Creates YOLO TXT annotation files")
print("- Beginner Friendly\n")

print("2. Roboflow")
print("- Online annotation platform")
print("- Supports dataset management")
print("- Image augmentation")
print("- Export datasets in YOLO format\n")

print("3. CVAT")
print("- Computer Vision Annotation Tool")
print("- Suitable for large datasets")
print("- Supports image and video annotation")
print("- Used by many industries\n")


# ============================================================
# Practical Task 3
# Sample Dataset Structure
# ============================================================

print("\n========== Dataset Structure ==========\n")

dataset_structure = """
dataset/
│
├── images/
│   ├── train/
│   │     helmet1.jpg
│   │     helmet2.jpg
│   │
│   └── val/
│         helmet3.jpg
│
└── labels/
    ├── train/
    │     helmet1.txt
    │     helmet2.txt
    │
    └── val/
          helmet3.txt
"""

print(dataset_structure)


# ============================================================
# Practical Task 4
# Sample data.yaml
# ============================================================

print("\n========== data.yaml ==========\n")

data_yaml = """
train: dataset/images/train
val: dataset/images/val

nc: 1

names:
  - helmet
"""

print(data_yaml)


# ============================================================
# Practical Task 5
# Train Custom YOLO Model
# ============================================================

from ultralytics import YOLO

# Load pretrained YOLO model
model = YOLO("yolov8n.pt")

# Train the model
model.train(
    data="data.yaml",
    epochs=10
)

print("\nTraining Started Successfully!")