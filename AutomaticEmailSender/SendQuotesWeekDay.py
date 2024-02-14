import random
import datetime as dt
import smtplib
import config as c
def get_random_quote():
    with open("quotes.txt", "r") as quotes_file:
        quotes = quotes_file.readlines()
        return random.choice(quotes)

def send_email(email_list, quote):

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=c.send_email, password=c.password)
        connection.sendmail(
            from_addr=c.send_email,
            to_addrs=email_list,
            msg=f"Subject:Quote for the day\n\n{quote}."
        )

def get_emails():
    with open("emails_for_quotes.txt", "r") as email_file:
        emails = email_file.readlines()
        return emails
def main():
    day = dt.datetime.now().weekday()
    if day == 2:
        quote = get_random_quote()
        email_list = get_emails()
        if len(email_list) == 0:
            print('No emails found')
        else:
            send_email(email_list, quote)

main()