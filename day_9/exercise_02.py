travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country,times,cities):

    travel_log.append({"country": country, "visits": times, "cities": cities})




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("United States", 4, ["Orlando", "San Diego"])
add_new_country("Argentina", 2, ["Buenos Aires"])
add_new_country("Spain", 1, ["Barcelona"])

print(travel_log)


