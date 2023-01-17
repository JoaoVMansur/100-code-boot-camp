from art import  logo

print(logo)
print("Welcome to the secrect auction program.")
biders ={}
continuation = "yes"

while continuation == "yes":

    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    biders[name] = bid
    
    continuation = input("Are there any other bidders?: type 'yes' or 'no'\n").lower()

bets = []
for bet in biders.values():
    bets.append(bet)

higher = max(bets)
for name,bid in biders.items():
    if  bid == higher:
        print(f"The winner is {name} with a bid of ${bid} ")