import pandas
import datetime as dt
import smtplib
import config as c
import random
def get_birthdays():
    data = pandas.read_csv("birthdays.csv")
    birthday_dictionary = data.to_dict(orient="records")
    for birthday in birthday_dictionary:
        now = dt.datetime.now()
        if now.month != birthday.get("month") or now.day != birthday.get("day"):
            birthday_dictionary.remove(birthday)

    return birthday_dictionary

def send_birthday_email(to_email, msg, name):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=c.send_email, password=c.password)
        connection.sendmail(
            from_addr=c.send_email,
            to_addrs=to_email,
            msg=f"Subject:Happy Birthday {name}\n\n{msg}."
        )

def prepare_template(template_name, name):
    with open(template_name, "r") as template:
        template_data = template.read().replace("[NAME]", name)
        return template_data
def main():
    bd_list = get_birthdays()
    for bd in bd_list:
        number = random.randint(0, 3)
        print(f"number is {number}")
        template_name = f"letter_templates/letter_{number}.txt"
        name = bd.get("name")
        template = prepare_template(template_name, name)
        send_birthday_email(bd.get("email"), template, name)
        print(f"template {template_name} chosen randomly")


main()