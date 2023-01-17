from data import menu 
from data import resources

total = 0
def money():
    
    quarter = int(input("how many quartes?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    global total
    total = (quarter*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)

    return total  


def check_espresso(user_action):
    if menu[user_action]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enought water.")
        return False
    elif menu[user_action]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enought coffee")
        return False
    else:
        return True
    
def check_latte(user_action):
    if menu[user_action]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enought water.")
    elif menu[user_action]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enought coffee")
    elif menu[user_action]["ingredients"]["milk"] > resources["milk"]:
        print("there is not enought milk.")
    else:
        return True

def check_cappuccino(user_action):
    if menu[user_action]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enought water.")
    elif menu[user_action]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enought coffee")
    elif menu[user_action]["ingredients"]["milk"] > resources["milk"]:
        print("there is not enought milk.")
    else:
        return True
def check_money(user_action):
    print("Please inset coins.")
    if money() < menu[user_action]["cost"]:
        print("Sorry that's not enought money. Money refunded.")
        return False
    else:
        resources["money"] += menu[user_action]["cost"]
        return True
def remove_ingridients(user_action):
    if user_action == "espresso":
        resources["water"] -= menu[user_action]["ingredients"]["water"]
        resources["coffee"] -= menu[user_action]["ingredients"]["coffee"]

    else:
        resources["water"] -= menu[user_action]["ingredients"]["water"]
        resources["coffee"] -= menu[user_action]["ingredients"]["coffee"]
        resources["milk"] -=  menu[user_action]["ingredients"]["milk"]

function = 1
while function == 1: 
    user_action = input("“What would you like? (espresso/latte/cappuccino): ")  
    
    if user_action == "espresso":
        if check_espresso(user_action) == True:
            if check_money(user_action) == True:
                remove_ingridients(user_action)
                print(f"Here is ${round(total-menu[user_action]['cost'], 2)} in change.")
                print("Here is your expresso.Enjoy!")
    elif user_action == "latte":
        if check_latte(user_action) == True:
           if check_money(user_action) == True:
                remove_ingridients(user_action)
                print(f"Here is ${round(total-menu[user_action]['cost'], 2)} in change.")
                print("Here is your latte.Enjoy!")
    elif user_action == "cappuccino":
        if check_cappuccino(user_action) == True:
            if check_money(user_action) == True:
                remove_ingridients(user_action)
                print(f"Here is ${round(total-menu[user_action]['cost'], 2)} in change.")
                print("Here is your cappuccino.Enjoy!")
    elif user_action == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
    elif user_action == "off":
        break
    
    