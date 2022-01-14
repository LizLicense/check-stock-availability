#!/usr/local/bin/python3
from datetime import datetime
from logging import NullHandler
from bs4 import BeautifulSoup
import time
import requests
import SendMail


# return a status of availability of a product
def status (url, headers):
    respond = requests.get(url, headers=headers)
    # print('HTTP', respond.status_code)
    html = respond.content
    soup = BeautifulSoup(html, 'lxml')
    match = soup.find('button', class_='btn_bk')
    try:
        matchText = match.text
        if matchText == 'ADD TO CART':
            return 'inStock'               
    except:
        return 'no stock'

# have stock
url2 = 'https://en.mlb-korea.com/product/monogram-hobo-bag-new-york-yankees/2448/'
# no stock
url3 = 'https://m.en.mlb-korea.com/product/monogram-hobo-bag-new-york-yankees/2449/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
html = requests.get(url3,headers=headers)
print('HTTP', html.status_code)

counter = 0
status_list = []  

while True:
    counter += 1
    status_list = [status(url3, headers)]  #[e.g.: Sold out, Add to Cart] could be one of the examples
    time.sleep(1)
    print(datetime.now())
    body = "Item is in stock" # Add to Cart
    print(body)

    print('Number of visit: {0}\n'.format(counter))

    print("check Stock: ", status_list)
    if 'inStock' in status_list:
        SendMail.sentmail()
        print("Sending email to you now....\n")
    time.sleep(86400)
