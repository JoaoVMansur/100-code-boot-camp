print("Welcome to Python Pizza Delivery!\n")
size = input("What size do you want? s,m or l\n")
pepperoni = input("Do you want pepperoni? y or n\n")
cheese = input("Do you want extra cheese? y or n\n")

if size == "s":
    p_size = 15
elif size == "m":
    p_size = 20
elif size == "l":
    p_size = 25
if pepperoni == "y":
    if size == "s":
        p_pepperoni = 2
    else:
        p_pepperoni = 3    
       
else:
    p_pepperoni = 0
if cheese == "y":
    p_cheese = 1
else:
    p_cheese = 0

price = p_size + p_pepperoni + p_cheese    
print(f"your total bill is ${price}")
