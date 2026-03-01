import pandas as pd
import os
from sklearn.linear_model import LinearRegression
import numpy as np

print("Running Market Trend Forecast...")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

input_path = os.path.join(BASE_DIR, "data", "processed", "daily_sentiment_index.csv")

df = pd.read_csv(input_path)

# Sort by date to ensure correct order
df = df.sort_values("date")

# Create time index
df["time_index"] = range(len(df))

X = df[["time_index"]]
y = df["sentiment_score"]

# Train linear regression
model = LinearRegression()
model.fit(X, y)

slope = model.coef_[0]

# Predict next day's sentiment
next_day_index = np.array([[len(df)]])
next_day_prediction = model.predict(next_day_index)[0]

# Determine trend
if slope > 0:
    trend = "Bullish Trend 📈"
elif slope < 0:
    trend = "Bearish Trend 📉"
else:
    trend = "Stable Trend ➖"

print("\n--- Market Forecast Result ---")
print("Trend Direction:", trend)
print("Trend Slope:", round(slope, 4))
print("Predicted Next Day Sentiment:", round(next_day_prediction, 4))