import smtplib, ssl
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

username = os.getenv("EMAIL_USERNAME")
password = os.getenv("EMAIL_PASSWORD")

host = "smtp.gmail.com"
port = 465

context = ssl.create_default_context()


def send_email(message: str) -> None:
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        if username is not None and password is not None:
            server.login(username, password)
            server.sendmail(username, username, message)
