import pandas as pd





# data = pd.read_csv("day 25/weather_data.csv")

# data_dictionary = data.to_dict()

# print(data_dictionary)

# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data["temp"].max())
# #Get data in colums
# print(data.condition)

#Get data in row

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]

# print((monday.temp*(9/5))+32)

#create a dataframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]

# }

# data = pd.DataFrame(data_dict)

# data.to_csv("day 25/new_data.csv")

# print(data)

data = pd.read_csv("day 25/lesson/squirrel_data.csv")

#Primary Fur Color

fur = data["Primary Fur Color"]
gray = 0
black = 0
red = 0


for color in fur:
    if color == "Gray":
        gray +=1
    elif color == "Black":
        black +=1
    elif color == "Cinnamon":
        red += 1

squirrel_count = {
    
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray, red, black]

}
squirrel_data = pd.DataFrame(squirrel_count)
squirrel_data.to_csv("day 25/lesson/squirrel_count.csv")