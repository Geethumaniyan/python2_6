# ==========================================
# AI/ML Internship - Day 53
# Module 7: Stemming & Lemmatization
# ==========================================

# Install NLTK before running:
# pip install nltk

import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download WordNet (Only first time)
nltk.download('wordnet')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("=" * 60)
print("AI/ML Internship - Day 53")
print("Module 7: Stemming & Lemmatization")
print("=" * 60)

# -------------------------------------------------
# Theory Question 1
# -------------------------------------------------
print("\n1. What is Stemming?\n")
print("Stemming is the process of removing prefixes or")
print("suffixes from words to obtain their root form.")

# -------------------------------------------------
# Theory Question 2
# -------------------------------------------------
print("\n2. What is Lemmatization?\n")
print("Lemmatization converts words into their")
print("dictionary base form (lemma).")
print("It produces meaningful and valid words.")

# -------------------------------------------------
# Theory Question 3
# -------------------------------------------------
print("\n3. Difference Between Stemming and Lemmatization\n")

print("{:<20}{:<20}".format("Stemming", "Lemmatization"))
print("-" * 50)
print("{:<20}{:<20}".format("Fast", "Slower"))
print("{:<20}{:<20}".format("Simple Rules", "Dictionary Based"))
print("{:<20}{:<20}".format("Less Accurate", "More Accurate"))
print("{:<20}{:<20}".format("May give invalid words", "Produces valid words"))

# -------------------------------------------------
# Theory Question 4
# -------------------------------------------------
print("\n4. Why is Lemmatization More Accurate?\n")
print("Lemmatization uses dictionary meanings and")
print("language rules to produce meaningful root words.")
print("It improves NLP model accuracy.")

# -------------------------------------------------
# Theory Question 5
# -------------------------------------------------
print("\n5. Three Examples of Root Word Conversion\n")

examples = [
    ("Playing", "Play"),
    ("Running", "Run"),
    ("Children", "Child")
]

for original, root in examples:
    print(f"{original} --> {root}")

# =================================================
# Practical Task 1
# =================================================
print("\n" + "=" * 60)
print("Practical Task 1")
print("NLTK Installation Command")
print("=" * 60)

print("pip install nltk")

# =================================================
# Practical Task 2
# =================================================
print("\n" + "=" * 60)
print("Practical Task 2")
print("Stemming")
print("=" * 60)

words = ["Playing", "Working", "Learning", "Running"]

for word in words:
    print(f"{word:12} --> {stemmer.stem(word.lower())}")

# =================================================
# Practical Task 3
# =================================================
print("\n" + "=" * 60)
print("Practical Task 3")
print("Lemmatization")
print("=" * 60)

words = ["Cars", "Children", "Mice", "Dogs"]

for word in words:
    print(f"{word:12} --> {lemmatizer.lemmatize(word.lower())}")

# =================================================
# Practical Task 4
# =================================================
print("\n" + "=" * 60)
print("Practical Task 4")
print("Stemming vs Lemmatization")
print("=" * 60)

compare_words = [
    "playing",
    "running",
    "studies",
    "cars",
    "children",
    "mice"
]

print("{:<15}{:<15}{:<15}".format("Word", "Stemmed", "Lemmatized"))
print("-" * 45)

for word in compare_words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)
    print("{:<15}{:<15}{:<15}".format(word, stem, lemma))

# =================================================
# Practical Task 5
# =================================================
print("\n" + "=" * 60)
print("Practical Task 5")
print("Table of 10 Words")
print("=" * 60)

table_words = [
    "playing",
    "played",
    "running",
    "cars",
    "children",
    "mice",
    "studies",
    "dogs",
    "books",
    "working"
]

print("{:<15}{:<15}{:<15}".format("Word", "Stemmed", "Lemmatized"))
print("-" * 45)

for word in table_words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)
    print("{:<15}{:<15}{:<15}".format(word, stem, lemma))

# =================================================
# Bonus Example
# =================================================
print("\n" + "=" * 60)
print("Bonus Example")
print("=" * 60)

sentence = "The boys are playing footballs"

print("Original Sentence:")
print(sentence)

tokens = sentence.split()

print("\nTokens:")
print(tokens)

print("\nStemmed Words:")
stemmed = [stemmer.stem(word.lower()) for word in tokens]
print(stemmed)

print("\nLemmatized Words:")
lemmatized = [lemmatizer.lemmatize(word.lower()) for word in tokens]
print(lemmatized)

print("\n" + "=" * 60)
print("Day 53 Tasks Completed Successfully!")
print("=" * 60)