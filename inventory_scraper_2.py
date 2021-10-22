from lxml import html
import requests
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

matching_items = []
offset = 0

for num in range(0,20):
    page = requests.get('https://www.lcbapps.lcb.state.pa.us/webapp/Product_Management/psi_ProductInventory_Inter.asp?cdeNo=6946' + '&offset=' + str(offset))
    tree = html.fromstring(page.content)
    new_items = tree.xpath('//td[@colspan="4"]/text()')
    if len(new_items) > 0:
        for item in new_items:
            matching_items.append(item)
        offset = offset + 10
    else:
        break

if "Allegheny" in matching_items:
    port = 465  # For SSL
    # Create a secure SSL context
    context = ssl.create_default_context()
    sender = "blantonswebscraper@gmail.com"
    receiver = "jamesmcfadden111@gmail.com"
    email = MIMEMultipart('test')
    email["Subject"] = "Blanton's availability notification"
    email["From"] = sender
    email["To"] = receiver
    email_body = """<pre>
    Blanton's is available in Allegheny County!
    Go to the page: <a href="https://www.lcbapps.lcb.state.pa.us/webapp/Product_Management/psi_ProductInventory_Inter.asp?cdeNo=6946">Blanton's availability page</a>
    </pre>"""
    email_content = MIMEText(email_body ,'html')
    email.attach(email_content)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("blantonswebscraper@gmail.com", "")
        server.sendmail(sender, 'jamesmcfadden111@gmail.com', email.as_string())
        server.sendmail(sender, 'johnbelancic@gmail.com', email.as_string())

if "Washington" in matching_items:
    port = 465  # For SSL
    # Create a secure SSL context
    context = ssl.create_default_context()
    sender = "blantonswebscraper@gmail.com"
    receiver = "jamesmcfadden111@gmail.com"
    email = MIMEMultipart('test')
    email["Subject"] = "Blanton's availability notification"
    email["From"] = sender
    email["To"] = receiver
    email_body = """<pre>
    Blanton's is available in Washington County!
    Go to the page: <a href="https://www.lcbapps.lcb.state.pa.us/webapp/Product_Management/psi_ProductInventory_Inter.asp?cdeNo=6946">Blanton's availability page</a>
    </pre>"""
    email_content = MIMEText(email_body ,'html')
    email.attach(email_content)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("blantonswebscraper@gmail.com", "Summer$2020")
        server.sendmail(sender, 'jamesmcfadden111@gmail.com', email.as_string())
        server.sendmail(sender, 'johnbelancic@gmail.com', email.as_string())
# else:
#     port = 465  # For SSL
#     # Create a secure SSL context
#     context = ssl.create_default_context()
#     sender = "blantonswebscraper@gmail.com"
#     receiver = "jamesmcfadden111@gmail.com"
#     email = MIMEMultipart('test')
#     email["Subject"] = "Blanton's availability notification"
#     email["From"] = sender
#     email["To"] = receiver
#     email_body = """<pre>
#         Scan is completed - no Blanton's in Allegheny County.
#         </pre>"""
#     email_content = MIMEText(email_body ,'html')
#     email.attach(email_content)
#     with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#         server.login("blantonswebscraper@gmail.com", "Summer$2020")
#         server.sendmail(sender, 'jamesmcfadden111@gmail.com', email.as_string())
