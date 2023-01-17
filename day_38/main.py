from dotenv import load_dotenv
import requests
import os
from datetime import datetime
load_dotenv()
exercise_text = input("what exercise did you do today?: ")
nutritionix_params = {
    "query": exercise_text,
    "gender":os.getenv("GENDER"),
    "weight_kg":os.getenv("WEIGHT_KS"),
    "height_cm":os.getenv("HEIGHT_CM"),
    "age":os.getenv("AGE"),
}
sheety_header = {
    "Authorization": os.getenv("SHEETY_BAERER"),
}
nutritinix_header = {
    "x-app-id": os.getenv("NUTRININIX_ID"),
    "x-app-key": os.getenv("NUTRININIX_KEY"),
    
  
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url = exercise_endpoint, json=nutritionix_params,headers=nutritinix_header)
data = response.json()["exercises"][0]

sheets_params = {
    "página1":
        {"date": datetime.today().strftime("%d/%m/%Y"),
        "exercise": data["name"].title(),
        "duration(min)": data["duration_min"],
        "calories": data["nf_calories"]
    }   
}


add_exercise = requests.post(url=os.getenv("SHEETY_URL"), json=sheets_params, headers=sheety_header)

