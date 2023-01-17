from game_data import data
from random import randint

a = data[randint(0, 49)]
b = data[randint(0, 49)]
print(f"{a['follower_count']}")
print(f"{b['follower_count']}")

if a["follower_count"]>b["follower_count"]:
    print("higher")