from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from time import sleep
import requests
import json
import csv
import array


_URL = 'https://www.tutorcircle.hk/getCaseListData_default.php'
r = requests.get(_URL, verify = False)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.content, 'html.parser')
print(soup)

with open('test.csv','w',newline='',encoding='utf-8-sig') as f:
    w = csv.writer(f)
    temp = [soup.text]
    f.writerow(temp)