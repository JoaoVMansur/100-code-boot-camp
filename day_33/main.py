import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758
# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)
# print(iss_position)

params = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted": 0
}


response = requests.get("https://api.sunrise-sunset.org/json", params= params)
response.raise_for_status()
data = response.json()
sun_rise = data["results"]["sunrise"]
sun_set = data["results"]["sunset"]

print(sun_rise)
print(sun_set)
time_now = datetime.now()

