##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
TODAY = (now.month, now.day)
EMAIL = "pythonteste84@gmail.com"
PASSWORD = "pratinha123"
data = pandas.read_csv("day 32/birthday-wisher-extrahard-start/birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if TODAY in birthday_dict:
    birthday_person = birthday_dict[TODAY]
    file_path = f"day 32/birthday-wisher-extrahard-start/letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr= EMAIL, to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{content}"
        )