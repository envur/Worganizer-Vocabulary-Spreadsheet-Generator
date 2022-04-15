from .imports import *
from ..schemas.users import UserResetPassEmail
from .email_message import html_message
import hashlib


def email_sender(user: UserResetPassEmail, username: str, token: str):
    message_html = html_message("reset", os.environ["URL_LINK"], username, token)
    port = os.environ["PORT"]
    sender_email = os.environ["SENDER_EMAIL"]
    password = os.environ["EMAIL_PASS"]
    message = MIMEMultipart("alternative")
    message['Subject'] = "Reset Password"
    message['From'] = "Worganizer"
    message['To'] = user.email
    html = MIMEText(message_html, 'html')
    message.attach(html)
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, user.email, message.as_string())
            server.quit()
    except:
        raise exc.EMAIL_SENDING_FAILED