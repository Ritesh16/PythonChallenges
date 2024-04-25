import smtplib
import os
from dotenv import load_dotenv, dotenv_values

class EmailSender:
    def __init__(self):
        load_dotenv()
        self.sender_email =  os.getenv("sender_email")
        self.sender_password = os.getenv("sender_password")
        self.port = int(os.getenv("port"))
        self.host = os.getenv("host")

    def send_email(self, email_body, to_email):
        with smtplib.SMTP(self.host, port=self.port) as connection:
            connection.starttls()
            connection.login(user=self.sender_email, password=self.sender_password)
            connection.sendmail(
                from_addr=self.sender_email,
                to_addrs=to_email,
                msg=f"Subject:Stock price changed \n\n{email_body}."
            )