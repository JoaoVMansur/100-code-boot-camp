import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
computer_number = random.randint(1, 100)
def level():
    if difficulty == "hard":
        attempts = 5
    elif difficulty == "easy":
        attempts = 10
    return attempts



attempts = level()

guess = 0
while guess != computer_number:
    if attempts ==0:
        break

    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))


    def compare():

        global attempts
    
        if guess > computer_number:
            print("Too high.\nGuess again")
            attempts-= 1
        elif guess < computer_number:
            print("Too low.\nGuess again")
            attempts -= 1
    compare()




if attempts == 0:
    print(f"You've run out of guesses, you lose.\nThe number was {computer_number}")
elif guess == computer_number:
    print(f"You got it! The answer was {computer_number}")