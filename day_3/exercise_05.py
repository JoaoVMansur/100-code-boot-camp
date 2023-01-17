print("Welcome to love calculator!")
y_name = input("What is your name?\n").lower()
t_name = input("What is their name?\n").lower()


true_count_you = y_name.count("t") + y_name.count("r") + y_name.count("u") + y_name.count("e") 
true_count_their = t_name.count("t") + t_name.count("r") + t_name.count("u") + t_name.count("e")
love_count_you = y_name.count("l") + y_name.count("o") + y_name.count("v") + y_name.count("e")
love_count_their = t_name.count("l") + t_name.count("o") + t_name.count("v") + t_name.count("e")

love_score_1 = (true_count_you + true_count_their)
love_score_2 = (love_count_you + love_count_their)

final_love_score = int(f"{love_score_1}{love_score_2}")
if final_love_score < 10 or final_love_score > 90:
    print(f"Your score is {final_love_score}, you go together like coke and mentos.")
elif final_love_score >= 40 and final_love_score <=50:
    print(f"Your score is {final_love_score}, you are alright together.")
else:
    print(f"your score is {final_love_score}")