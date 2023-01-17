print("Welcome to the tip calculator.")
Bill = float(input("What was the total bill? $"))
Percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
Divided = int(input("How many people to splitt the bill? "))
bill_for_each = (Bill / Divided) * ((Percent / 100) + 1)
finall_amount = "{:.2f}".format(bill_for_each)
print("each person should pay: $" + finall_amount)
        