# ==========================================================
# AI/ML Internship - Day 55
# Module 7: TF-IDF (Term Frequency - Inverse Document Frequency)
# ==========================================================

# Install Scikit-Learn before running:
# pip install scikit-learn

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd

print("=" * 60)
print("AI/ML Internship - Day 55")
print("Module 7: TF-IDF")
print("=" * 60)

# ----------------------------------------------------------
# Documents
# ----------------------------------------------------------

documents = [
    "AI is amazing",
    "AI is powerful",
    "Machine learning is amazing"
]

# ----------------------------------------------------------
# Practical Task 1
# Bag of Words
# ----------------------------------------------------------

print("\nPractical Task 1 - Bag of Words")

bow = CountVectorizer()
bow_matrix = bow.fit_transform(documents)

print("\nVocabulary:")
print(bow.get_feature_names_out())

print("\nBoW Matrix:")
print(bow_matrix.toarray())

# ----------------------------------------------------------
# Practical Task 2
# TF-IDF
# ----------------------------------------------------------

print("\nPractical Task 2 - TF-IDF")

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(documents)

print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())

# ----------------------------------------------------------
# Practical Task 3
# Print Vocabulary
# ----------------------------------------------------------

print("\nPractical Task 3 - Vocabulary")

print(tfidf.get_feature_names_out())

# ----------------------------------------------------------
# Practical Task 4
# Compare BoW and TF-IDF
# ----------------------------------------------------------

print("\nPractical Task 4 - Comparison")

print("\nBag of Words:")
print(bow_matrix.toarray())

print("\nTF-IDF:")
print(tfidf_matrix.toarray())

# ----------------------------------------------------------
# Practical Task 5
# Important Words
# ----------------------------------------------------------

print("\nPractical Task 5 - Important Words")

feature_names = tfidf.get_feature_names_out()

for i, doc in enumerate(documents):
    print(f"\nDocument {i+1}: {doc}")

    scores = tfidf_matrix[i].toarray()[0]

    word_scores = list(zip(feature_names, scores))
    word_scores.sort(key=lambda x: x[1], reverse=True)

    for word, score in word_scores:
        if score > 0:
            print(f"{word:12} : {score:.3f}")

print("\nProgram Completed Successfully!")