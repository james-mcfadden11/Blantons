from lxml import html
import requests
# import smtplib, ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

page = requests.get('https://www.finewineandgoodspirits.com/webapp/wcs/stores/servlet/StoreStateSearch?storeId=10051&langId=-1&catalogId=10051&ItemCode=000007728&SearchNow=on&ProdName=Wild+Turkey+Straight+Bourbon+81+Proof&fromURL=%2Fwebapp%2Fwcs%2Fstores%2Fservlet%2FCatalogSearchResultView%3FstoreId%3D10051%26catalogId%3D10051%26langId%3D-1%26categoryId%3D1334015%26variety%3DBourbon%26categoryType%3DSpirits%26top_category%3D%26parent_category_rn%3D%26sortBy%3D5%26searchSource%3DE%26pageView%3D%26beginIndex%3D&countyName=All+Stores&f=&storeName=All+Stores&pageNum=1&perPage=10&storeType=&city=&zip_code=&county=&storeNO=')
tree = html.fromstring(page.content)

new_items = tree.xpath('//span[@class="boldMaroonText"]/text()')
print(new_items)
