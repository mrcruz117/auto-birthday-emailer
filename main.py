# import smtplib
# from emails import my_gmail, gmail_password, my_icloud, icloud_password
#
# with smtplib.SMTP("smtp.gmail.com") as gmail_connection:
#     # icloud_connection = smtplib.SMTP("smtp.mail.me.com")
#
#     gmail_connection.starttls()
#     gmail_connection.login(user=my_gmail, password=gmail_password)
#     gmail_connection.sendmail(
#         from_addr=my_gmail,
#         to_addrs=my_icloud,
#         msg="Subject:Automated Email Test\n\nTest Message"
#     )


import datetime as dt

now = dt.datetime.now()

my_birthday = dt.datetime(month=11, day=7, year=1989)

print(my_birthday)
