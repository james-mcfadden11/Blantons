from lxml import html
import requests
import smtplib, ssl

# blanton's
# page = requests.get('https://www.finewineandgoodspirits.com/webapp/wcs/stores/servlet/SearchResultsView?categoryId=&storeId=10051&catalogId=10051&langId=-1&sType=SimpleSearch&resultCatEntryType=2&showResultsPage=true&searchSource=Q&variety=&pageView=&beginIndex=0&pageSize=15&sortBy=5&searchTerm=blantons&SearchKeyWord=blantons#facet:&productBeginIndex:0&orderBy:&pageView:&minPrice:&maxPrice:&pageSize:&')
# tester for search term "makers mark"
# page = requests.get('https://www.finewineandgoodspirits.com/webapp/wcs/stores/servlet/SearchResultsView?categoryId=&storeId=10051&catalogId=10051&langId=-1&sType=SimpleSearch&resultCatEntryType=2&showResultsPage=true&searchSource=Q&variety=&pageView=&beginIndex=0&pageSize=15&sortBy=5&searchTerm=makers+mark&SearchKeyWord=makers+mark#facet:&productBeginIndex:0&orderBy:&pageView:&minPrice:&maxPrice:&pageSize:&')
tree = html.fromstring(page.content)
no_results_box = tree.xpath('//div[@class="no_search_results_msg_container"]')
print(len(no_results_box))

if len(no_results_box) == 0:
    port = 465  # For SSL
    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("blantonswebscraper@gmail.com", "")
        server.sendmail("blantonswebscraper@gmail.com", "jamesmcfadden111@gmail.com", "Blanton's is available!")
