print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '`" ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Tresure Island.")
print("Your mission is to find the tresure.")

first_step = input("You're at a cross road where do you wanna go? Type 'left' or 'right'\n") 
first_step_1 = first_step.lower()
if first_step_1 == "left":
    second_step = input("You came to a lake. There is a islan in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n")
    second_step_1 = second_step.lower()
    if second_step_1 == "wait":
        third_step = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which one do you open?\n")
        third_step_1 = third_step.lower()
        if third_step_1 == "red":
            print("You entered on a burning room and died burned. Game over")
        elif third_step_1 == "blue":
            print("You entered a room of beasts. Game Over")
        else:
            print("You found the tresure congratualations. You Won")
                
    
    
    else:
        print("A crocodile found and ate you. Game Over")    
          

else:
    print("You fell into a hole and died. Game Over")
