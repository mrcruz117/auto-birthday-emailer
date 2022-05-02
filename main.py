import datetime as dt
import random
import smtplib
from emails import my_gmail, gmail_password, my_icloud

now = dt.datetime.now()

weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as gmail_connection:
        gmail_connection.starttls()
        gmail_connection.login(my_gmail, gmail_password)
        print("logged in")
        gmail_connection.sendmail(
            from_addr=my_gmail,
            to_addrs=my_icloud,
            msg=f"Subject: Motivation Quote\n\n{quote}"
        )
