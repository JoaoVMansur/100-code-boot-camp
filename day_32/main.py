import smtplib
import datetime as dt
import random
now = dt.datetime.now()
week = now.weekday()
if week == 0:
    data = open("day 32/quotes.txt", "r")
    quotes = data.readlines()
    msg = quotes[random.randint(0, len(quotes))]
    data.close()

my_email = "pythonteste84@gmail.com"
password = "pratinha123"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()

    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr= my_email, to_addrs= "jvictormansur@gmail.com", 
    msg=f"Subject:Monday Motivation Message\n\n{msg}")
