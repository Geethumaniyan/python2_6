# ==========================================
# AI/ML Internship - Day 52
# Module 7: Text Preprocessing
# Tokenization, Stop Words & Text Cleaning
# ==========================================

import string
import re

print("=" * 60)
print("AI/ML Internship - Day 52")
print("Module 7: Text Preprocessing")
print("=" * 60)

# -------------------------------------------------
# Theory Question 1
# -------------------------------------------------
print("\n1. Define Text Preprocessing\n")
print("Text Preprocessing is the process of converting raw text")
print("into a clean and understandable format for computers.")

# -------------------------------------------------
# Theory Question 2
# -------------------------------------------------
print("\n2. What is Tokenization?\n")
print("Tokenization is the process of breaking text into")
print("smaller units called tokens.")
print("Tokens can be words, sentences, or characters.")

# -------------------------------------------------
# Theory Question 3
# -------------------------------------------------
print("\n3. What are Stop Words?\n")
print("Stop words are commonly used words that usually")
print("do not add important meaning to a sentence.")
print("Examples: is, am, are, the, a, an, in, on, at")

# -------------------------------------------------
# Theory Question 4
# -------------------------------------------------
print("\n4. Why Remove Punctuation?\n")
print("Removing punctuation helps clean the text,")
print("reduces noise, and improves NLP model accuracy.")

# -------------------------------------------------
# Theory Question 5
# -------------------------------------------------
print("\n5. Why Convert Text to Lowercase?\n")
print("Lowercase conversion keeps text consistent.")
print("For example, 'AI' and 'ai' become the same word.")

# =================================================
# Practical Task 1
# =================================================
print("\n" + "=" * 60)
print("Practical Task 1 - Tokenization")
print("=" * 60)

text = "I love Machine Learning"
tokens = text.split()

print("Original Text :", text)
print("Tokens        :", tokens)

# =================================================
# Practical Task 2
# =================================================
print("\n" + "=" * 60)
print("Practical Task 2 - Lowercase Conversion")
print("=" * 60)

text = "HELLO WORLD"

print("Original :", text)
print("Lowercase:", text.lower())

# =================================================
# Practical Task 3
# =================================================
print("\n" + "=" * 60)
print("Practical Task 3 - Remove Punctuation")
print("=" * 60)

text = "Python!!! is Awesome???"

clean_text = text.translate(
    str.maketrans('', '', string.punctuation)
)

print("Original :", text)
print("Cleaned  :", clean_text)

# =================================================
# Practical Task 4
# =================================================
print("\n" + "=" * 60)
print("Practical Task 4 - Identify Stop Words")
print("=" * 60)

sentence = "The cat is sitting on the chair"

stop_words = [
    "the", "is", "am", "are", "was", "were",
    "a", "an", "in", "on", "at", "of", "to",
    "for", "and", "or", "with", "from"
]

words = sentence.lower().split()

identified = [word for word in words if word in stop_words]

print("Sentence   :", sentence)
print("Stop Words :", identified)

# =================================================
# Practical Task 5
# =================================================
print("\n" + "=" * 60)
print("Practical Task 5 - Clean Sentence")
print("=" * 60)

text = "AI 2025 is AMAZING!!!"

clean = text.lower()
clean = re.sub(r'[^a-zA-Z\s]', '', clean)

print("Original :", text)
print("Cleaned  :", clean)

# =================================================
# Bonus Example
# =================================================
print("\n" + "=" * 60)
print("Complete NLP Preprocessing Example")
print("=" * 60)

text = "Hello!!! AI 2025 is Amazing."

print("Original Text :", text)

# Lowercase
text = text.lower()

# Remove numbers and punctuation
text = re.sub(r'[^a-zA-Z\s]', '', text)

print("After Cleaning:", text)

# Tokenization
tokens = text.split()
print("Tokens:", tokens)

# Remove Stop Words
stop_words = {
    "is", "am", "are", "was", "were",
    "the", "a", "an", "of", "to",
    "for", "and", "or", "in", "on",
    "at", "with", "from"
}

filtered = [word for word in tokens if word not in stop_words]

print("After Stop Word Removal:", filtered)

print("\n" + "=" * 60)
print("Day 52 Tasks Completed Successfully!")
print("=" * 60)