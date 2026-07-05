# ==========================================
# AI/ML Internship - Day 51
# Module 7: Introduction to NLP
# ==========================================

print("=" * 60)
print("AI/ML Internship - Day 51")
print("Module 7: Introduction to NLP")
print("=" * 60)

# -------------------------------------------------
# Theory Question 1
# -------------------------------------------------
print("\n1. What is NLP?\n")
print("Natural Language Processing (NLP) is a branch of Artificial Intelligence")
print("that enables computers to understand, process, analyze, and generate")
print("human language.")

# -------------------------------------------------
# Theory Question 2
# -------------------------------------------------
print("\n2. Why do we need NLP?\n")
print("We need NLP because computers understand binary data (0s and 1s),")
print("while humans communicate using natural languages like English,")
print("Malayalam, Hindi, and Tamil. NLP acts as a bridge between")
print("humans and computers.")

# -------------------------------------------------
# Theory Question 3
# -------------------------------------------------
print("\n3. Explain three NLP applications.\n")

print("1. Chatbots")
print("   - Chatbots answer user questions automatically.")
print("   - Example: ChatGPT")

print("\n2. Language Translation")
print("   - Converts one language into another.")
print("   - Example: English to Malayalam")

print("\n3. Sentiment Analysis")
print("   - Identifies whether a text is Positive, Negative, or Neutral.")

# -------------------------------------------------
# Theory Question 4
# -------------------------------------------------
print("\n4. Difference between NLP and Computer Vision\n")

print("{:<25}{}".format("NLP", "Computer Vision"))
print("-" * 50)
print("{:<25}{}".format("Works with text", "Works with images/videos"))
print("{:<25}{}".format("Processes language", "Processes images"))
print("{:<25}{}".format("Chatbots", "Object Detection"))
print("{:<25}{}".format("Translation", "Face Detection"))

# -------------------------------------------------
# Theory Question 5
# -------------------------------------------------
print("\n5. What is Text Data?\n")
print("Text data is information represented using words,")
print("sentences, and language. NLP mainly works with")
print("structured and unstructured text.")

# =================================================
# Practical Task 1
# =================================================
print("\n" + "=" * 60)
print("Practical Task 1")
print("10 NLP Applications Used in Daily Life")
print("=" * 60)

applications = [
    "1. ChatGPT",
    "2. Google Assistant",
    "3. Siri",
    "4. Alexa",
    "5. Gmail Spam Detection",
    "6. Google Translate",
    "7. WhatsApp Predictive Text",
    "8. YouTube Comment Analysis",
    "9. Amazon Review Analysis",
    "10. Customer Support Chatbots"
]

for app in applications:
    print(app)

# =================================================
# Practical Task 2
# =================================================
print("\n" + "=" * 60)
print("Practical Task 2")
print("Five Apps that Use NLP")
print("=" * 60)

apps = [
    "ChatGPT",
    "Google Assistant",
    "Siri",
    "Alexa",
    "Google Translate"
]

for i, app in enumerate(apps, start=1):
    print(f"{i}. {app}")

# =================================================
# Practical Task 3
# =================================================
print("\n" + "=" * 60)
print("Practical Task 3")
print("20 Positive Reviews")
print("=" * 60)

positive_reviews = [
    "Excellent product.",
    "Amazing quality.",
    "Very useful.",
    "Highly recommended.",
    "Fantastic experience.",
    "Loved it.",
    "Works perfectly.",
    "Very satisfied.",
    "Great value for money.",
    "Easy to use.",
    "Beautiful design.",
    "Fast delivery.",
    "Outstanding performance.",
    "Superb customer service.",
    "Very comfortable.",
    "Impressive quality.",
    "Worth buying.",
    "Exceeded my expectations.",
    "Five-star product.",
    "I will buy again."
]

for review in positive_reviews:
    print("-", review)

print("\n" + "=" * 60)
print("20 Negative Reviews")
print("=" * 60)

negative_reviews = [
    "Poor quality.",
    "Very disappointed.",
    "Waste of money.",
    "Not recommended.",
    "Terrible experience.",
    "Stopped working.",
    "Bad packaging.",
    "Very slow.",
    "Low quality.",
    "Too expensive.",
    "Product was damaged.",
    "Not worth the price.",
    "Customer service was poor.",
    "Delivery was late.",
    "Doesn't work properly.",
    "Very frustrating.",
    "Cheap material.",
    "Not as expected.",
    "I want a refund.",
    "One-star product."
]

for review in negative_reviews:
    print("-", review)

# =================================================
# Practical Task 4
# =================================================
print("\n" + "=" * 60)
print("Practical Task 4")
print("How ChatGPT Uses NLP")
print("=" * 60)

paragraph = """
ChatGPT uses Natural Language Processing (NLP) to understand,
analyze, and generate human language. It reads the user's input,
understands its meaning and context, and produces meaningful,
accurate, and conversational responses. NLP enables ChatGPT to
answer questions, translate languages, summarize text, write code,
and assist users in various real-world tasks.
"""

print(paragraph)

# =================================================
# Practical Task 5
# =================================================
print("=" * 60)
print("Practical Task 5")
print("NLP Workflow")
print("=" * 60)

print("""
            Text Data
                |
                V
         Text Cleaning
                |
                V
        Text Processing
                |
                V
      Feature Extraction
                |
                V
        Model Training
                |
                V
           Prediction
""")

print("=" * 60)
print("Day 51 Tasks Completed Successfully!")
print("=" * 60)