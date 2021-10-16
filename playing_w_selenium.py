from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import re


driver = webdriver.Safari()
# blantons
# driver.get("https://www.finewineandgoodspirits.com/webapp/wcs/stores/servlet/ProductDisplay?catalogId=10051&storeId=10051&productId=1944836&langId=-1&partNumber=000006946prod&errorViewName=ProductDisplayErrorView&categoryId=1334015&top_category=25208&parent_category_rn=1334013&urlLangId=&variety=Bourbon&categoryType=Spirits&fromURL=%2fwebapp%2fwcs%2fstores%2fservlet%2fCatalogSearchResultView%3fstoreId%3d10051%26catalogId%3d10051%26langId%3d-1%26categoryId%3d1334015%26variety%3dBourbon%26categoryType%3dSpirits%26top_category%3d25208%26parent_category_rn%3d1334013%26sortBy%3d5%26searchSource%3dE%26pageView%3d%26beginIndex%3d0")

# wild turkey
driver.get("https://www.finewineandgoodspirits.com/webapp/wcs/stores/servlet/ProductDisplay?catalogId=10051&storeId=10051&productId=1942816&langId=-1&partNumber=000005127prod&errorViewName=ProductDisplayErrorView&categoryId=1334015&top_category=25208&parent_category_rn=1334013&urlLangId=&variety=Bourbon&categoryType=Spirits&fromURL=%2fwebapp%2fwcs%2fstores%2fservlet%2fCatalogSearchResultView%3fstoreId%3d10051%26catalogId%3d10051%26langId%3d-1%26categoryId%3d1334015%26variety%3dBourbon%26categoryType%3dSpirits%26top_category%3d%26parent_category_rn%3d%26sortBy%3d5%26searchSource%3dE%26pageView%3d%26beginIndex%3d0")
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

print("navigating to store availability")
time.sleep(5)

# select county
select = Select(driver.find_element_by_xpath("//*[@id='countyNames']"))
print("selected county drop-down menu")
select.select_by_value("02")
print("selected Allegheny county")

time.sleep(5)

# submit
print("clicking submit")
driver.find_element_by_xpath("//*[@id='main_container']/div[4]/form[1]/div[2]/div[6]/div").click()
time.sleep(5)

######## if more than 10 stores in Allegheny county have Blantons, only the first 10
######## will populate here - need ot update this eventually to make more flexible
######## for other bottles, counties, etc.

stores = []

# should be 9 thru 19 for page with 10 results
# add conditional for less than 10 results on the page
for div in range(9, 19):
    result_str = ""
    store_id = driver.find_element_by_xpath("//*[@id='main_container']/div[4]/div[" + str(div) + "]/div[1]/div[2]/span[2]")
    store_id_str = store_id.get_attribute('innerHTML')[1:5]
    result_str += "Store ID: " + store_id_str + "\n"

    address_phone = driver.find_element_by_xpath("//*[@id='main_container']/div[4]/div[" + str(div) + "]/div[1]/div[2]/span[3]")
    address_phone_str = address_phone.get_attribute('innerHTML')
    # remove html tags
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    address_phone_str = re.sub(cleanr, '', address_phone_str)
    # remove tabs
    address_phone_str = address_phone_str.replace("\t", "")
    result_str += address_phone_str + "\n"

    driver.find_element_by_xpath("//*[@id='main_container']/div[4]/div[" + str(div) + "]/div[1]/div[5]/a").click()
    time.sleep(5)
    available_units = driver.find_element_by_xpath("//*[@id='main_container']/div[4]/div[11]/div[4]")
    available_units_str = available_units.get_attribute('innerHTML')
    available_units_str = re.sub(cleanr, '', available_units_str)
    available_units_str = available_units_str.replace("\t", "")
    available_units_str = available_units_str.replace("\n", "")
    available_units_str = available_units_str.strip()


    result_str += available_units_str + " available\n"
    driver.back()
    time.sleep(5)

    print(result_str)


    # stores.append(result_str)


# print(stores)


# Johnny: online only offerings?
# address line 2 needs line break


time.sleep(5)


driver.close()
