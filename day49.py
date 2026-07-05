"""
AI/ML Internship - Day 49
Module 6: Understanding Epochs, Training Results, Loss Graphs,
Precision, Recall & mAP in YOLO Training

Name:
Date:
"""

# ============================================================
# THEORY ANSWERS
# ============================================================

print("=" * 60)
print("DAY 49 - THEORY ANSWERS")
print("=" * 60)

print("\n1. What is an Epoch?")
print("Answer:")
print("An epoch is one complete pass of the entire training dataset through the YOLO model.")

print("\n2. What is Loss?")
print("Answer:")
print("Loss is a measure of how wrong the model's predictions are.")
print("Lower loss indicates better learning and improved model performance.")

print("\n3. What is Precision?")
print("Answer:")
print("Precision measures how many detected objects are actually correct.")
print("Formula: Precision = Correct Detections / Total Detections")

print("\n4. What is Recall?")
print("Answer:")
print("Recall measures how many actual objects were successfully detected.")
print("Formula: Recall = Detected Objects / Actual Objects")

print("\n5. What is mAP?")
print("Answer:")
print("mAP stands for Mean Average Precision.")
print("It combines Precision and Recall into a single evaluation metric.")
print("Higher mAP indicates better object detection performance.")

# ============================================================
# PRACTICAL TASK 1
# Train a YOLO Model
# ============================================================

print("\n" + "=" * 60)
print("PRACTICAL TASK 1")
print("=" * 60)

print("""
Train Command:

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="data.yaml",
    epochs=10,
    imgsz=640
)
""")

print("Observe during training:")
print("- Epoch")
print("- Loss")
print("- Precision")
print("- Recall")
print("- mAP")

# ============================================================
# PRACTICAL TASK 2
# Locate Training Files
# ============================================================

print("\n" + "=" * 60)
print("PRACTICAL TASK 2")
print("=" * 60)

print("After training, locate these files:")

print("""
runs/
└── detect/
    └── train/
        ├── best.pt
        ├── last.pt
        └── results.png
""")

# ============================================================
# PRACTICAL TASK 3
# Analyze Training Graphs
# ============================================================

print("\n" + "=" * 60)
print("PRACTICAL TASK 3")
print("=" * 60)

print("Ideal Training Graph Analysis:")

print("""
Loss       -> Should decrease.
Precision  -> Should increase.
Recall     -> Should increase.
mAP        -> Should increase.
""")

# ============================================================
# PRACTICAL TASK 4
# Compare Epoch 1 vs Epoch 10
# ============================================================

print("\n" + "=" * 60)
print("PRACTICAL TASK 4")
print("=" * 60)

print("{:<15}{:<15}{:<15}".format("Metric", "Epoch 1", "Epoch 10"))
print("-" * 45)
print("{:<15}{:<15}{:<15}".format("Loss", "High", "Low"))
print("{:<15}{:<15}{:<15}".format("Precision", "Low", "High"))
print("{:<15}{:<15}{:<15}".format("Recall", "Low", "High"))
print("{:<15}{:<15}{:<15}".format("mAP", "Low", "High"))

# ============================================================
# PRACTICAL TASK 5
# Why Loss Decreases
# ============================================================

print("\n" + "=" * 60)
print("PRACTICAL TASK 5")
print("=" * 60)

print("""
Loss decreases during training because the model learns from its mistakes.
After each epoch, YOLO updates its weights using backpropagation and gradient descent,
allowing it to make more accurate predictions.
As training progresses, prediction errors become smaller,
resulting in lower loss values.
""")

print("\n" + "=" * 60)
print("DAY 49 TASK COMPLETED")
print("=" * 60)