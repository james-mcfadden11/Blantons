from lxml import html
import requests
import smtplib, ssl

port = 465  # For SSL
# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("blantonswebscraper@gmail.com", "")
    server.sendmail("blantonswebscraper@gmail.com", "jamesmcfadden111@gmail.com", "Welcome to the Blanton's availability mailing list! This program automatically checks the availability of Blanton's in Pennsylvania and emails you when it becomes available. Be sure to set alerts for emails from this sender to be informed the moment Blanton's becomes available in PA liquor stores.\n\n\n Note also John Belancic has a tiny microscopic weiner.")
    server.sendmail("blantonswebscraper@gmail.com", "johnbelancic@gmail.com", "Welcome to the Blanton's availability mailing list! This program automatically checks the availability of Blanton's in Pennsylvania and emails you when it becomes available. Be sure to set alerts for emails from this sender to be informed the moment Blanton's becomes available in PA liquor stores.\n\n\n Note also John Belancic has a tiny microscopic weiner.")
