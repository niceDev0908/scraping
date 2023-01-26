from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from time import sleep
import requests
import json
import csv
import array


_URL = 'https://www.tutorcircle.hk/getCaseListData_default.php'
r = requests.get(_URL, verify = True)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.content, 'html.parser')
whole = soup.text
tels = whole.split('\"tel\":\"')
ids = whole.split('\"id\":\"')
with open('1.csv','w',newline='',encoding='utf-8-sig') as f:
    w = csv.writer(f)
    count = 0
    for tel in tels:
        if count ==0:
            count = count + 1
            continue
        info = [ids[count][:6], tel[:8]]
        w.writerow(info)
        count = count + 1
    

