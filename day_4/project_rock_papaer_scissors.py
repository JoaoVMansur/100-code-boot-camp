import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper ='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = int(input("What to you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. "))
moves = [rock,paper,scissors]

if choice >= 3 or choice < 0:
    print("You tiped a invalid number, You lost")
else:
    print(moves[choice])
    print("computer choose: ")
    n_moves = len(moves)
    computer_moves = random.randint(0,n_moves-1)
    print(moves[computer_moves])
    if choice == 0 and computer_moves == 2:
        print("You win")
    elif choice > computer_moves:
        print("You win") 
    elif choice == computer_moves:
        print("It's a draw")
    else:
        print("You lose")

    



# if choice == 0:
#     print(rock)
# elif choice == 1:
#     print(paper)
# else:
#     print(scissors)
# print("computer choose: ")
# n_moves = len(moves)
# computer_moves = random.randint(0,n_moves-1)
# print(moves[computer_moves])
# if computer_moves == 0:
#     print(rock)
# elif computer_moves == 1:
#     print(paper)
# else:
#     print(scissors)
# if choice == 0 and computer_moves == 2:
#     print("You win")
# elif choice > computer_moves:
#     print("You win")
# elif choice == computer_moves:
#     print("It's a draw")
# else:
#     print("You lose")
