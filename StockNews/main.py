import os
import requests
from dotenv import dotenv_values, load_dotenv

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.getenv("STOCK_API_KEY")

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, stock_params)
response.raise_for_status()

stock_data = response.json()["Time Series (Daily)"]
data = [value for(key, value) in stock_data.items()]

# Get closing costs differences
previous_day_closing_cost = float(data[0]['4. close'])
day_before_previous_day_closing_cost = float(data[1]['4. close'])

difference = abs(previous_day_closing_cost - day_before_previous_day_closing_cost)
print(difference)

# Get difference percentage
difference_percentage = float((difference/previous_day_closing_cost) * 100)

if difference_percentage > 5:
    print("Get news!")
