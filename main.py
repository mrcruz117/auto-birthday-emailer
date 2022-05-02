import datetime as dt
import random
import smtplib
import pandas
from emails import my_gmail, gmail_password, my_icloud

today = dt.datetime.now()
month_day = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

# birthdays_dict = {(birthday_month, birthday_day): data_row}
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

print(birthdays_dict)

if month_day in birthdays_dict:
    birthday_person = birthdays_dict[month_day]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as gmail_connection:
        gmail_connection.starttls()
        gmail_connection.login(my_gmail, gmail_password)
        print("logged in")
        gmail_connection.sendmail(
            from_addr=my_gmail,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
