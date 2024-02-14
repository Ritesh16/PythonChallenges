import smtplib
import config as c

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=c.send_email, password=c.password)
    connection.sendmail(
        from_addr=c.send_email,
        to_addrs="",
        msg="Subject:hello\n\nThis is body of the email."
    )