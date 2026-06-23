# ==========================================
# AI/ML Internship - Day 43
# Support Vector Machine (SVM)
# Complete Tasks Solution
# ==========================================

import pandas as pd
from sklearn.svm import SVC

# ==========================================
# TASK 1 - THEORY ANSWERS
# ==========================================

print("\n========== TASK 1 : THEORY ANSWERS ==========\n")

print("1. What is SVM?")
print("SVM (Support Vector Machine) is a supervised machine learning algorithm used for classification and regression tasks.\n")

print("2. What is a Decision Boundary?")
print("A decision boundary is a line or plane that separates different classes.\n")

print("3. What are Support Vectors?")
print("Support vectors are the data points closest to the decision boundary.\n")

print("4. What is Margin?")
print("Margin is the distance between support vectors and the decision boundary.\n")

print("5. Advantages of SVM?")
print("- High Accuracy")
print("- Works well with small datasets")
print("- Effective for classification")
print("- Handles high-dimensional data")
print("- Good generalization\n")


# ==========================================
# TASK 2 - DATASET CREATION
# ==========================================

print("\n========== TASK 2 : DATASET CREATION ==========\n")

# Student Result Dataset
student_data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}

student_df = pd.DataFrame(student_data)

print("Student Result Dataset")
print(student_df)
print()

# Disease Dataset
disease_data = {
    "Temperature": [98, 99, 100, 102, 103, 104],
    "Disease": [0, 0, 0, 1, 1, 1]
}

disease_df = pd.DataFrame(disease_data)

print("Disease Dataset")
print(disease_df)
print()

# Spam Dataset
spam_data = {
    "Message_Length": [20, 25, 30, 150, 180, 200],
    "Spam": [0, 0, 0, 1, 1, 1]
}

spam_df = pd.DataFrame(spam_data)

print("Spam Detection Dataset")
print(spam_df)
print()


# ==========================================
# TASK 3 - MODEL BUILDING
# ==========================================

print("\n========== TASK 3 : MODEL BUILDING ==========\n")

X = student_df[["Hours"]]
y = student_df["Result"]

student_model = SVC()
student_model.fit(X, y)

prediction = student_model.predict([[4]])

print("Prediction for 4 Study Hours:", prediction)
print()


# ==========================================
# TASK 4 - PREDICTION PRACTICE
# ==========================================

print("\n========== TASK 4 : PREDICTION PRACTICE ==========\n")

# Student Result Prediction
student_prediction = student_model.predict([[6]])
print("Student Result Prediction:", student_prediction)

# Disease Prediction
X_disease = disease_df[["Temperature"]]
y_disease = disease_df["Disease"]

disease_model = SVC()
disease_model.fit(X_disease, y_disease)

disease_prediction = disease_model.predict([[103]])
print("Disease Status Prediction:", disease_prediction)

# Spam Prediction
X_spam = spam_df[["Message_Length"]]
y_spam = spam_df["Spam"]

spam_model = SVC()
spam_model.fit(X_spam, y_spam)

spam_prediction = spam_model.predict([[170]])
print("Spam Detection Prediction:", spam_prediction)


# ==========================================
# TASK 5 - ALGORITHM COMPARISON
# ==========================================

print("\n========== TASK 5 : ALGORITHM COMPARISON ==========\n")

comparison = pd.DataFrame({
    "Algorithm": [
        "Logistic Regression",
        "KNN",
        "Decision Tree",
        "Random Forest",
        "SVM"
    ],
    "Advantages": [
        "Simple and Fast",
        "Easy to Understand",
        "Easy Visualization",
        "High Accuracy",
        "High Accuracy and Good for High-Dimensional Data"
    ],
    "Disadvantages": [
        "Less Effective for Complex Data",
        "Slow Prediction",
        "Can Overfit",
        "More Computational Cost",
        "Slow on Large Datasets"
    ]
})

print(comparison)


# ==========================================
# TASK 6 - VISUALIZATION ACTIVITY
# ==========================================

print("\n========== TASK 6 : VISUALIZATION ==========\n")

print("Decision Boundary:")
print("● ● ● ● | ▲ ▲ ▲ ▲")

print("\nSupport Vectors:")
print("● ● ● ● | ▲ ▲ ▲ ▲")
print("      ^     ^")
print("Support Vectors")

print("\nMargin:")
print("● ● ●   ||   ▲ ▲ ▲")
print("        ||")
print("      Margin")

print("\n========== DAY 43 TASK COMPLETED ==========")