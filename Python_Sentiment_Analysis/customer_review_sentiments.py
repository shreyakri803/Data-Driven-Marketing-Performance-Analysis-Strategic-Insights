import pandas as pd
import nltk
import pyodbc
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# nltk.download('vader_lexicon')

def fetching_data_from_sql():
    conn_str = (
        "Driver= {ODBC Driver 17 for SQL Server};"
        "Server= GILL\\SQLEXPRESS;"
        "Database=PortfolioProject_MarketingAnalytics;"  
        "Trusted_Connection=yes;" 
    )
    conn = pyodbc.connect(conn_str)
    query = "SELECT ReviewID, CustomerID, ProductID, ReviewDate, Rating, ReviewText FROM customer_reviews"

    df = pd.read_sql(query, conn)
    conn.close()
    return df

customer_reviews_df = fetching_data_from_sql()

sia = SentimentIntensityAnalyzer()

def calculatingSentimentScores(review):
    sentiment = sia.polarity_scores(review)
    return sentiment['compound']

def Categorizing_sentiments(score, rating):
    if score > 0.05:
        if rating >= 4: 
            return "Positive"
        elif rating == 3:
            return "Mixed Positive"
        else:
            return "Mixed Negative"
    
    elif score < -0.05:
        if rating <= 2:
            return "Negative"
        elif rating == 3:
            return "Mixed Negative"
        else:
            return "Mixed Positive"
        
    else:
        return "Neutral"

def defining_bucket(score):
    if score >= 0.5:
        return "0.5 to 1"       # Strong Positive
    elif 0.0 <= score < 0.5:
        return "0.0 to 0.49"    # Moderately Positive
    elif -0.5 < score < 0.0:
        return "-0.49 to 0.0"   # Moderately Negative
    else:
        return "-1 to -0.5"     # Fixed incorrect range

# Apply sentiment analysis functions
customer_reviews_df['SentimentScores'] = customer_reviews_df["ReviewText"].map(calculatingSentimentScores)

customer_reviews_df["SentimentCategory"] = customer_reviews_df.apply(
    lambda row: Categorizing_sentiments(row["SentimentScores"], row["Rating"]), axis=1
)

customer_reviews_df["SentimentBucket"] = customer_reviews_df['SentimentScores'].map(defining_bucket)

print(customer_reviews_df.head())

customer_reviews_df.to_csv('fact_customer_reviews_with_sentiment.csv', index=False)