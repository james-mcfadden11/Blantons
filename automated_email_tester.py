import smtplib
import ssl

print('imported everything')

port = 465  # For SSL

# Create a secure SSL context
context = ssl.create_default_context()

print('made it to with statement')

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("blantonswebscraper@gmail.com", "")
    server.sendmail("blantonswebscraper@gmail.com", "jamesmcfadden111@gmail.com", "Test 123")
