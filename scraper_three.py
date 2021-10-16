from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import re
from lxml import html
import requests
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

driver = webdriver.Safari()
# blantons
# driver.get("https://www.finewineandgoodspirits.com/webapp/wcs/stores/servlet/ProductDisplay?catalogId=10051&storeId=10051&productId=1944836&langId=-1&partNumber=000006946prod&errorViewName=ProductDisplayErrorView&categoryId=1334015&top_category=25208&parent_category_rn=1334013&urlLangId=&variety=Bourbon&categoryType=Spirits&fromURL=%2fwebapp%2fwcs%2fstores%2fservlet%2fCatalogSearchResultView%3fstoreId%3d10051%26catalogId%3d10051%26langId%3d-1%26categoryId%3d1334015%26variety%3dBourbon%26categoryType%3dSpirits%26top_category%3d25208%26parent_category_rn%3d1334013%26sortBy%3d5%26searchSource%3dE%26pageView%3d%26beginIndex%3d0")

# wild turkey
driver.get("https://www.finewineandgoodspirits.com/webapp/wcs/stores/servlet/ProductDisplay?catalogId=10051&storeId=10051&productId=1942816&langId=-1&partNumber=000005127prod&errorViewName=ProductDisplayErrorView&categoryId=1334015&top_category=25208&parent_category_rn=1334013&urlLangId=&variety=Bourbon&categoryType=Spirits&fromURL=%2fwebapp%2fwcs%2fstores%2fservlet%2fCatalogSearchResultView%3fstoreId%3d10051%26catalogId%3d10051%26langId%3d-1%26categoryId%3d1334015%26variety%3dBourbon%26categoryType%3dSpirits%26top_category%3d%26parent_category_rn%3d%26sortBy%3d5%26searchSource%3dE%26pageView%3d%26beginIndex%3d0")

# buffalo trace bourbon cream
# driver.get("https://www.finewineandgoodspirits.com/webapp/wcs/stores/servlet/ProductDisplay?catalogId=10051&storeId=10051&productId=1939584&langId=-1&partNumber=000001408prod&errorViewName=ProductDisplayErrorView&categoryId=&top_category=&parent_category_rn=&urlLangId=&categoryType=Spirits&fromURL=%2fwebapp%2fwcs%2fstores%2fservlet%2fCatalogSearchResultView%3fstoreId%3d10051%26catalogId%3d10051%26langId%3d-1%26sType%3dSimpleSearch%26resultCatEntryType%3d2%26showResultsPage%3dtrue%26pageSize%3d15%26sortBy%3d5%26searchSource%3dQ%26pageView%3d%26beginIndex%3d0%26searchTerm%3dbuffalo%2btrace%26SearchKeyWord%3dbuffalo%2btrace")

print("accessed site")
time.sleep(10)

# close "enter your email" notification
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
time.sleep(2)

# click "yes" for age verification
driver.find_element_by_xpath("//*[@id='ageVerify']/div[4]/p").click()
print("age verified")
time.sleep(2)

# if the following xpath exists, navigate to store availability, if not, end script
try:
    driver.find_element_by_xpath("//*[@id='leftPanel']/div/div[4]/div[3]/div[4]/div[2]/div[2]/a").click()
except:
    print("out of stock - closing session")
    time.sleep(5)
    driver.close()
    quit()

print("navigating to store availability")
time.sleep(5)

# select county
select = Select(driver.find_element_by_xpath("//*[@id='countyNames']"))
print("selected county drop-down menu")
# 02 is allegheny county
select.select_by_value("02")
print("selected Allegheny county")

time.sleep(5)

# submit
print("clicking submit")
driver.find_element_by_xpath("//*[@id='main_container']/div[4]/form[1]/div[2]/div[6]/div").click()
time.sleep(5)

# 10 or more results looks different
# with div[9] thru div[19] instead of 6 thru 16
# will need to update this for flexibility on number of results

result_str = ""

for div in range(9, 19):
    try:
        # for >10 results
        store_id = driver.find_element_by_xpath("//*[@id='main_container']/div[4]/div[" + str(div) + "]/div[1]/div[2]/span[2]")
        # store_id = driver.find_element_by_xpath("//*[@id='main_container']/div[4]/div[4]/div[" + str(div) + "]/div[1]/div[2]/span[2]")
        store_id_str = store_id.get_attribute('innerHTML')[1:5]
        result_str += "Store ID: " + store_id_str + "\n"
        print("store ID accessed and saved")

        # for >10 results
        address_phone = driver.find_element_by_xpath("//*[@id='main_container']/div[4]/div[" + str(div) + "]/div[1]/div[2]/span[3]")
        # address_phone = driver.find_element_by_xpath("//*[@id='main_container']/div[4]/div[4]/div[" + str(div) + "]/div[1]/div[2]/span[3]")
        address_phone_str = address_phone.get_attribute('innerHTML')
        # remove html tags
        cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        address_phone_str = re.sub(cleanr, '', address_phone_str)
        # remove tabs
        address_phone_str = address_phone_str.replace("\t", "")
        result_str += address_phone_str + "\n"
        print("address and phone accessed and saved")

        # for >10 results
        driver.find_element_by_xpath("//*[@id='main_container']/div[4]/div[" + str(div) + "]/div[1]/div[5]/a").click()
        # driver.find_element_by_xpath("//*[@id='main_container']/div[4]/div[4]/div[" + str(div) + "]/div[1]/div[5]/a").click()
        time.sleep(5)
        available_units = driver.find_element_by_xpath("//*[@id='main_container']/div[4]/div[11]/div[4]")
        available_units_str = available_units.get_attribute('innerHTML')
        available_units_str = re.sub(cleanr, '', available_units_str)
        available_units_str = available_units_str.replace("\t", "")
        available_units_str = available_units_str.replace("\n", "")
        available_units_str = available_units_str.strip()
        result_str += available_units_str + " available\n\n"
        print("available units accessed and saved")

        driver.back()
        time.sleep(8)

    except:
        print("error received - it is possible all results are captured, or no results for this county")
        break


time.sleep(5)
driver.close()

# if there were any results
if result_str != "":
    # send email
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
    email_body = "Blanton's is available in Allegheny County at the following store(s)\n\n" + result_str

    # html or plain as second argument of MIMEText()
    email_content = MIMEText(email_body, 'plain')
    email.attach(email_content)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("blantonswebscraper@gmail.com", "Summer$2020")
        server.sendmail(sender, 'jamesmcfadden111@gmail.com', email.as_string())


    print("email sent")

# check results in terminal
print(result_str)
