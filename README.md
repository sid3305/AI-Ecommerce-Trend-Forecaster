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

## Milestone 1 Completed

- Real-time data ingestion
- Data cleaning and preprocessing
- Structured dataset ready for sentiment analysis

Next: Sentiment Analysis Engine