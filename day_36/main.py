import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

stock_endpoint = "https://www.alphavantage.co/query?"
news_endpoint = "https://newsapi.org/v2/everything?"

stock_params = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":os.getenv("STOCK"),
    "outputsize":"compact",
    "interval":"60min",
    "apikey":os.getenv("ALPHA_API_KEY"),
    
}
news_params = {
    "q": os.getenv("COMPANY_NAME"),
    "searching":"title",
    "apikey":os.getenv("NEWS_API_KEY"),
}
request = requests.get(stock_endpoint, stock_params)
data = request.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]

yesterday_closing_price = float(data_list[0]["4. close"])
before_yesterday_closing_price = float(data_list[1]["4. close"])

difference = yesterday_closing_price-before_yesterday_closing_price
up_down = None
if difference > 0:
    up_down = "up"
else:
    up_down = "down"

diff_percent = round((difference/yesterday_closing_price)*100)
if abs(diff_percent) > 0:
   

    news_request = requests.get(news_endpoint, news_params)
    articles = news_request.json()["articles"][:3]


    formatted_articles = [f"{os.getenv('STOCK')}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief {article['description']}" for article in articles]

    client = Client(os.getenv("ACCOUNT_SID"),os.getenv("AUTH_TOKEN"))
    for article in formatted_articles:
        message = client.messages.create(
            body = article,
            from_= os.getenv("TWILIO_PHONE_NUMBER"),
            to = os.getenv("MY_PHONE_NUMBER")
        )