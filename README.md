# review-sentiment-analyzer
Sentiment Analysis with Google Cloud Natural Language API

This project performs sentiment analysis on product reviews using the Google Cloud Natural Language API.

## Files Included

- `reviews.txt`: Sample product reviews.
- `sentiment_analysis.py`: Script to perform sentiment analysis.
- `requirements.txt`: Project dependencies.
- `.gitignore`: Git ignore rules.

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Khushi-Chaudhary04/review-sentiment-analyzer.git
   cd review-sentiment-analyzer
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   # source venv/bin/activate  # MacOS/Linux
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up Google Cloud API key:**
   - Enable the Natural Language API in your Google Cloud project.
   - Generate an API key from the Google Cloud Console.
   - Replace `YOUR_API_KEY` in `sentiment_analysis.py` with your API key.

5. **Run the script:**
   ```sh
   python sentiment_analysis.py
   ```

6. **View results:**
   - Open `sentiment_results.csv` to see the sentiment analysis results.
