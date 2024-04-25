import os
import requests
from dotenv import dotenv_values, load_dotenv
from email_sender import EmailSender

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# API Constants
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

receiver_email = os.getenv("receiver_email")

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

# Get difference percentage
difference_percentage = float((difference/previous_day_closing_cost) * 100)

if difference_percentage > 1:
    # get news data
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = response.json()["articles"]

    top_3_news_articles = news_data[:3]

    #format articles
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}".encode("utf-8") for article in top_3_news_articles]

    email = EmailSender()

    # Send email
    email.send_email(formatted_articles, receiver_email)