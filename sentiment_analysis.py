import requests
import pandas as pd

# Set your Google Cloud API key
api_key = 'YOUR_API_KEY'

def analyze_sentiment(review):
    url = f"https://language.googleapis.com/v1/documents:analyzeSentiment?key={api_key}"
    document = {
        "document": {
            "type": "PLAIN_TEXT",
            "content": review
        },
        "encodingType": "UTF8"
    }
    response = requests.post(url, json=document)
    sentiment = response.json()['documentSentiment']['score']
    return "positive" if sentiment > 0 else "negative" if sentiment < 0 else "neutral"

# Read reviews from file
with open('reviews.txt', 'r') as file:
    reviews = file.readlines()

# Analyze sentiment for each review
results = []
for review in reviews:
    sentiment = analyze_sentiment(review.strip())
    results.append({'Review': review.strip(), 'Sentiment': sentiment})

# Save results to a new text file
df = pd.DataFrame(results)
df.to_csv('sentiment_results.csv', index=False)

print("Sentiment analysis complete. Results saved to sentiment_results.csv")
