# ==========================================================
# AI/ML Internship - Day 54
# Module 7: Bag of Words (BoW)
# ==========================================================

# Install Scikit-Learn before running:
# pip install scikit-learn

from sklearn.feature_extraction.text import CountVectorizer

print("=" * 60)
print("AI/ML Internship - Day 54")
print("Module 7: Bag of Words (BoW)")
print("=" * 60)

# ----------------------------------------------------------
# Practical Task 1
# Create Vocabulary
# ----------------------------------------------------------

print("\nPractical Task 1 - Vocabulary Creation")

documents = [
    "AI is powerful",
    "AI is amazing"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(documents)

print("Vocabulary:")
print(vectorizer.get_feature_names_out())

# ----------------------------------------------------------
# Practical Task 2
# Manual BoW Vector
# ----------------------------------------------------------

print("\nPractical Task 2 - Manual BoW Vector")

vocabulary = ["I", "love", "AI", "Python"]
sentence = ["I", "love", "AI"]

vector = []

for word in vocabulary:
    vector.append(sentence.count(word))

print("Vocabulary :", vocabulary)
print("Sentence   :", sentence)
print("BoW Vector :", vector)

# ----------------------------------------------------------
# Practical Task 3
# CountVectorizer Example
# ----------------------------------------------------------

print("\nPractical Task 3 - CountVectorizer")

documents = [
    "I love AI",
    "I love Python"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(documents)

print("\nVocabulary:")
print(vectorizer.get_feature_names_out())

print("\nBoW Matrix:")
print(X.toarray())

# ----------------------------------------------------------
# Practical Task 4
# Generate BoW for 5 Sentences
# ----------------------------------------------------------

print("\nPractical Task 4 - BoW for Five Sentences")

sentences = [
    "AI is amazing",
    "Python is powerful",
    "I love AI",
    "Machine learning is fun",
    "AI and Python are useful"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(sentences)

print("\nVocabulary:")
print(vectorizer.get_feature_names_out())

print("\nBoW Matrix:")
print(X.toarray())

# ----------------------------------------------------------
# Additional Example
# ----------------------------------------------------------

print("\nAdditional Example")

reviews = [
    "Amazing movie",
    "Bad movie",
    "Amazing acting",
    "Bad acting",
    "Movie is amazing"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(reviews)

print("\nVocabulary:")
print(vectorizer.get_feature_names_out())

print("\nBoW Matrix:")
print(X.toarray())

print("\nProgram Completed Successfully!")