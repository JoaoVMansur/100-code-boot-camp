height = int(input("What is your height in cm?\n"))
ticket = 0
if height >= 120:
    print("can ride")
    age = int(input("What is your age\n"))
    if age < 12:
        ticket = 5
        print("tickes for childrem are $5")
    elif age <= 18:
        ticket = 7
        print("tickes for youngs are $7")
    else:
        ticket = 12
        print("tickes for adult are $12")


    photo = input("Do you want a photo taken? Y or N ")
    a_photo = photo.lower()

    if a_photo == "y":
       ticket += 3
       print(f"your ticket will be ${ticket}")
    else:
        ticket += 0
        print(f"your ticket will be ${ticket}")

else:
    print("can't ride")        