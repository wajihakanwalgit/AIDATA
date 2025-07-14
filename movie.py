import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

from textblob import TextBlob

from colorama import init, Fore

import time
import sys
init(autoreset=True)
def load_data():
    try:
        data = pd.read_csv('movie_data.csv')
        return data
    except FileNotFoundError:
        print(Fore.RED + "Error: movie_data.csv not found.")
        sys.exit(1)
    df['combined_features'] = df['Genre'].fillna("") + ' ' + df['Overview'].fillna("")
    return df
movies_df = load_data()
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
def list_genres(df):
    genres = movies_df['Genre'].unique()
    print(Fore.CYAN + "Available Genres:")
    for genre in genres:
        print(Fore.YELLOW + f"- {genre}")
list_genres(movies_df)
def recommend_movies(genre=None, mood=None, rating=None, num_recommendations=5):
    filtered_df = movies_df.copy()
    if genre:
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case=False, na=False)]
    if mood:
        filtered_df = filtered_df[filtered_df['Mood'].str.contains(mood, case=False, na=False)]
    if rating:
        filtered_df = filtered_df[filtered_df['Rating'] >= rating]
    # Compute similarity scores
    tfidf_matrix = tfidf.fit_transform(filtered_df['combined_features'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    # Get recommendations
    recommendations = []
    for idx, row in filtered_df.iterrows():
        overview = row['Overview']
        if pd.isna(overview):
            continue
        polarity = TextBlob(overview).sentiment.polarity
        if polarity > 0:
            sentiment = "positive"
        elif polarity < 0:
            sentiment = "negative"
        else:
            sentiment = "neutral"
        recommendations.append((row['Title'], sentiment))
    return recommendations
if (mood and ((TextBlob(mood).sentiment.polarity < 0 and mood.lower() != "sad") or (TextBlob(mood).sentiment.polarity > 0 and mood.lower() != "happy"))):
    print(Fore.GREEN + "Your mood is positive! Here are some uplifting movie recommendations:")
    recommendations = recommend_movies(genre=genre, mood=mood, rating=rating)
    if len(recommendations) == 0:
        print(Fore.RED + "No recommendations found for the given criteria.")
def display_recommendations(recommendations):
    if not recommendations:
        print(Fore.RED + "No recommendations found.")
        return
    print(Fore.CYAN + "Here are some movie recommendations for you:")
    for title, sentiment in recommendations:
        print(Fore.GREEN + f"- {title} ({sentiment})")
