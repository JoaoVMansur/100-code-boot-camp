from data import menu 
from data import resources


def money():
    quarter = int(input("how many quartes?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles: "))
    pennies = int(input("how many pennies?: "))

    total = (quarter*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)

    return total  



def check_money(user_action):
    if money() < menu[user_action]["cost"]:
        print("Sorry that's not enought money. Money refunded.")
    else:
        resources["money"] += menu[user_action]["cost"]
    

user_action = input()

check_money(user_action)