from random import randint
from art import logo
from art import vs
from game_data import data

print(logo)
keep_going = 1          
score = 0
a = data[randint(0, 49)]
b = data[randint(0,49)]

while keep_going == 1:
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    if guess == "a" and a["follower_count"]>b["follower_count"]:
        score +=1
        print(f"You're right! Current score: {score}")
        a = b
        b = data[randint(0,49)]
    elif guess == "b" and b["follower_count"]>a["follower_count"]:
        score += 1
        print(f"You're right! Current score: {score}")
        a = b
        b = data[randint(0, 49)]
       
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break