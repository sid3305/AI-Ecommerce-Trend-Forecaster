# AI-Powered E-Commerce Trend & Sentiment Forecaster

This project collects real-time e-commerce news data, processes it, and performs sentiment analysis to detect market trends.

---

## Project Structure

E-commerce trend forecaster/
│
├── src/
│   ├── ingestion/
│   ├── preprocessing/
│   ├── sentiment/
│   └── topic_modeling/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

---

## Setup Instructions

### 1️⃣ Clone the repository

git clone <repo-url>

cd E-commerce trend forecaster

---

### 2️⃣ Create virtual environment

Windows:
python -m venv .venv
.venv\Scripts\activate

Mac/Linux:
python3 -m venv .venv
source .venv/bin/activate

---

### 3️⃣ Install dependencies

pip install -r requirements.txt

---

### 4️⃣ Create .env file

Create a file named `.env` in the root folder.

Add your NewsAPI key:

NEWS_API_KEY=your_actual_news_api_key_here

You can get your API key from:
https://newsapi.org

---

### 5️⃣ Run Data Ingestion

python src/ingestion/news_ingestion.py

This creates:
data/raw/news_data.csv

---

### 6️⃣ Run Preprocessing

python src/preprocessing/text_preprocessing.py

This creates:
data/processed/cleaned_news.csv

---

## Milestone 1 – Data Pipeline ✅

- Real-time data ingestion using NewsAPI
- Multi-brand e-commerce tracking
- Data cleaning and preprocessing
- Structured dataset ready for sentiment analysis

---

## Milestone 2 – Sentiment & Market Trend Engine ✅

### 🔹 Sentiment Models Implemented
- VADER (rule-based baseline)
- TextBlob (lexicon-based baseline)
- FinBERT (finance-aware transformer model)

### 🔹 Business-Oriented Sentiment Analysis
FinBERT is used to classify news articles into:
- Positive (favorable business impact)
- Neutral (no significant market impact)
- Negative (unfavorable business impact)

### 🔹 Daily Market Sentiment Index
- Article-level sentiment converted to numeric scores
- Aggregated into daily average sentiment index
- Creates time-series representation of market mood

### 🔹 Market Trend Forecasting
- Linear regression used to detect trend direction
- Classifies trend as:
  - Bullish 📈
  - Bearish 📉
  - Stable ➖
- Predicts next-day sentiment value

### 🔹 Visualization
- Raw sentiment trend plotting
- 7-day moving average smoothing
- Clear representation of market momentum shifts

---

## Current Capabilities

- Tracks sentiment across 17 major Indian e-commerce brands
- Detects shifts in overall e-commerce market mood
- Provides directional market signal (Bullish / Bearish)
- Generates interpretable sentiment trends for business analysis

---

## Next Phase (Planned Improvements)

- Insight generation layer (business interpretation engine)
- Brand-level trend comparison
- Automated pipeline execution
- Long-term historical sentiment tracking