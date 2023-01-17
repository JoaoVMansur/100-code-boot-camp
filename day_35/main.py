import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = os.getenv("API_KEY")
client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"))

weather_params = {
    "q":"Ansan", 
    "appid":api_key,
    "units":"metric",
    }

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()

day_weather = data["weather"][0]
day_temperature = data["main"]["temp"]

if day_weather["id"] < 700:
   
    message = client.messages.create(
  body="Get a umbrella it will rain today",
  from_=os.getenv("TWILIO_PHONE_NUMBER"),
  to=os.getenv("MY_PHONE_NUMBER")
)
    
else:
   
    message = client.messages.create(
  body="It will not rain today",
  from_=os.getenv("TWILIO_PHONE_NUMBER"),
  to=os.getenv("MY_PHONE_NUMBER")
    )
if day_temperature < 10:
    
    message = client.messages.create(
  body="its cold bring 롱패딩",
  from_=os.getenv("TWILIO_PHONE_NUMBER"),
  to=os.getenv("MY_PHONE_NUMBER")
)
elif day_temperature < 20 and day_temperature > 10:
    message = client.messages.create(
  body="its cold but not that much",
  from_=os.getenv("TWILIO_PHONE_NUMBER"),
  to=os.getenv("MY_PHONE_NUMBER")
)
    
    
elif day_temperature > 20:
    
    message = client.messages.create(
  body="its not cold today",
  from_=os.getenv("TWILIO_PHONE_NUMBER"),
  to=os.getenv("MY_PHONE_NUMBER")
)
    