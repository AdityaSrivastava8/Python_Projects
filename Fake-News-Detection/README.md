# Description :

Fake news has become a major issue in today's digital world,
where misleading information spreads rapidly through social
media and news websites. Manually verifying every news article
is difficult and time-consuming. Natural Language Processing
(NLP) and Machine Learning (ML) provide an efficient way to
automatically classify news articles as Real or Fake based on
their textual content.

This project uses NLP preprocessing techniques such as
Tokenization, Stopword Removal, Stemming, and TF-IDF
Vectorization before training a Multinomial Naive Bayes
classifier for fake news detection.

# Objective :

1. Preprocess news articles using NLP techniques.
2. Convert textual data into numerical features using TF-IDF.
3. Train a Machine Learning model to classify news as Real or Fake.
4. Predict the authenticity of new news articles entered by the user.
5. Evaluate the model using classification accuracy.

# Explanation of the Process :

1. **Dataset Loading:** The dataset is imported using the Pandas library.
2. **Text Preprocessing:** News articles are cleaned using tokenization, stopword removal, and stemming to improve text quality.
3. **Feature Extraction:** TF-IDF Vectorization converts textual data into numerical feature vectors that can be understood by the machine learning model.
4. **Model Training:** The processed data is divided into training and testing sets, and a Multinomial Naive Bayes classifier is trained.
5. **Model Evaluation:** The trained model predicts the labels of the test data, and its performance is measured using classification accuracy.
6. **Prediction:** Users can enter a new news article, which is processed using the same NLP pipeline before the model predicts whether it is **Real** or **Fake**.

# Tools & Technologies Used :

The following tools, libraries, and technologies were used to develop this project:

1. **Python** : Primary programming language used for implementing the project. 
2. **Pandas** : Used to load, organize, and manipulate the dataset. 
3. **NLTK (Natural Language Toolkit)** : Performs NLP tasks such as tokenization, stopword removal, and stemming. 
4. **Scikit-learn** : Provides TF-IDF Vectorization, train-test splitting, the Multinomial Naive Bayes classifier, and evaluation metrics. 
5. **TF-IDF Vectorizer** : Converts textual news articles into numerical feature vectors suitable for machine learning.
6. **Multinomial Naive Bayes** : Machine Learning algorithm used to classify news articles as Real or Fake.
7. **Google Colab** : Development environment used to write and execute the Python notebook. 
8. **GitHub** : Used for version control and hosting the project repository.

# Explaination of all the Steps : (Screenshots are uploaded too) :

1. Dataset Preview :

The dataset is loaded using the Pandas library and contains three main columns: Title, Text, and Label. The df.head() function is used to display the first five records, allowing us to verify that the data has been loaded correctly before preprocessing and model training begin.

CSV URL : https://raw.githubusercontent.com/AdityaSrivastava8/Python_Projects/refs/heads/main/Fake-News-Detection/fake_news.csv

2. Tokenization :

Tokenization is the process of breaking a news article into individual words or tokens. This is the first step in text preprocessing and helps the model analyze the text more effectively by treating each word as a separate unit.

3. Stopword Removal :

Stopword removal eliminates commonly used words such as the, is, and, and of, which usually do not contribute to determining whether a news article is real or fake. Removing these words reduces noise and improves the quality of the text data.

4. Stemming :

Stemming reduces words to their root form, such as playing → play or running → run. This decreases the vocabulary size and groups similar words together, improving the efficiency of the machine learning model.

5. Model Accuracy :

After training the Multinomial Naive Bayes classifier, the model is evaluated using the test dataset. The accuracy score represents the percentage of correctly classified news articles and provides an overall measure of the model's performance.

6. Real News Prediction :

The user enters a news article, which is processed using the same NLP pipeline and converted into TF-IDF features. The trained model analyzes these features and correctly classifies the article as Real.

7. Fake News Prediction :

Similarly, when a user enters a fake or misleading news article, it undergoes the same preprocessing and feature extraction steps. The trained model then predicts the article as Fake, demonstrating its ability to identify misleading information.

# Outcomes :

- Successfully developed a Fake News Detection system using Natural Language Processing (NLP) and Machine Learning.
- Implemented text preprocessing techniques including tokenization, stopword removal, and stemming.
- Converted textual data into numerical features using TF-IDF Vectorization.
- Trained a Multinomial Naive Bayes classifier to classify news articles as **Real** or **Fake**.
- Evaluated the model using classification accuracy and tested it on user-provided news articles.

# Learning & Difficulties :

# Learning
- Learned the fundamentals of NLP preprocessing and text classification.
- Gained hands-on experience with TF-IDF Vectorization and the Multinomial Naive Bayes algorithm.
- Improved understanding of building and evaluating a Machine Learning model.

# Difficulties
- Handling text preprocessing and dataset preparation.
- Managing NLTK resources and dependencies.
- Converting textual data into numerical features using TF-IDF.

# Future Aspects :

- Improve prediction accuracy using advanced machine learning and deep learning models.
- Develop a web application using Streamlit or Flask for real-time news prediction.
- Train the model on larger and more diverse datasets.
- Integrate live news APIs for real-time fake news detection.
