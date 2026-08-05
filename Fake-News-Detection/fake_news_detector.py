# ============================================================
#              FAKE NEWS DETECTION USING NLP
# ============================================================

# ============================================================
# Import Libraries
# ============================================================

# Import NLTK library for Natural Language Processing tasks.
import nltk

nltk.download('punkt')
nltk.download('punkt_tab') # Downloaded the latest version to prevent any error.
nltk.download('stopwords')

# ============================================================
# Load Dataset
# ============================================================

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/AdityaSrivastava8/Python_Projects/refs/heads/main/Fake-News-Detection/fake_news.csv")

# Display first five rows
print(df.head())

# ============================================================
# Tokenization
# ============================================================

# Tokenization splits a sentence into individual words (tokens),
# making it easier to perform further text preprocessing.

from nltk.tokenize import word_tokenize

# Select the first news article from the dataset.
text = df.loc[0, "Text"]

# Convert the article into individual words.
tokens = word_tokenize(text)

# Display tokenized words.
print(tokens)

# ============================================================
# Stopword Removal
# ============================================================

# Stopwords are common English words (such as "the", "is",
# "and", etc.) that usually do not contribute to identifying
# whether news is real or fake. Removing them reduces noise.

from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

filtered = [word for word in tokens if word.lower() not in stop_words]

print(filtered)

# ============================================================
# Stemming
# ============================================================

# Stemming converts words into their root form.
#
# Example:
# playing -> play
# running -> run
# studies -> studi
#
# This reduces vocabulary size and improves model performance.

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

stemmed = [stemmer.stem(word) for word in filtered]

print(stemmed)

# ============================================================
# TF-IDF Vectorization
# ============================================================

# Machine Learning models cannot understand raw text directly.
# TF-IDF converts each news article into numerical feature
# vectors by assigning higher importance to informative words.

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words="english")

# Convert all news articles into TF-IDF vectors.
X = vectorizer.fit_transform(df["Text"])

# Store target labels.
y = df["Label"]

# ============================================================
# Train-Test Split
# ============================================================

# Split the dataset into:
# 80% Training Data
# 20% Testing Data
#
# Training data is used to build the model while testing
# data evaluates its performance.

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ============================================================
# Train Machine Learning Model
# ============================================================

# Multinomial Naive Bayes is used because it is:
# - Fast
# - Efficient
# - Suitable for text classification
# - Performs well with TF-IDF features

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()

# Train the classifier.
model.fit(X_train, y_train)

# ============================================================
# Prediction & Accuracy
# ============================================================

# Predict labels for unseen news articles in the test dataset.

from sklearn.metrics import accuracy_score

pred = model.predict(X_test)

print(pred)

# Calculate classification accuracy.
print("Accuracy:", accuracy_score(y_test, pred))

# ============================================================
# Test on New News Article
# ============================================================

# The user enters a news article.
# Example : Scientists developed a new cancer treatment.
# It is converted into a TF-IDF vector using the same
# vectorizer before being classified as Real or Fake.

new_news = input("Enter a news article:\n")

new_vec = vectorizer.transform([new_news])

prediction = model.predict(new_vec)[0]

print("Prediction:", prediction)
