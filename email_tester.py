from lxml import html
import requests
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# For SSL
port = 465

# Create a secure SSL context
context = ssl.create_default_context()

sender = "blantonswebscraper@gmail.com"
receiver = "jamesmcfadden111@gmail.com"
email = MIMEMultipart('test')
email["Subject"] = "Test email"
email["From"] = sender
email["To"] = receiver
test_str = "this string was inserted in the email body"
email_body = "This is a test " + test_str + " more email body"

email_content = MIMEText(email_body ,'html')
email.attach(email_content)
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("blantonswebscraper@gmail.com", "")
    server.sendmail(sender, 'jamesmcfadden111@gmail.com', email.as_string())


print("email sent")
