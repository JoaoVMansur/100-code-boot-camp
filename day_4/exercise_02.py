import random
custumers = input("Give me everybody' names, separated by a comma.\n")
list_custumers = custumers.split(", ")
random_custumer = len(list_custumers)
payer = random.randint(0,random_custumer -1)
print(f"{list_custumers[payer]} is going to pay the bill today")


