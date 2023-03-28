import smtplib
import datetime as dt
import random


my_email = "yurekli.mertt@gmail.com"
password = "zpnhzclesluvpozk"


def send_email():
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ishakdemirtas12@gmail.com",
            msg=f"Subject:Tuesday Motivation\n\n{quote}"
        )


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 5:
    send_email()

