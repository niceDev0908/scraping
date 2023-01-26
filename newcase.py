from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from time import sleep
import json
import csv
import array


AllEntries = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=50)
    page = browser.new_page()
    page.goto('https://www.toptutor.hk/newcases')
    with open('newcase.csv','w',newline='',encoding='utf-8-sig') as f:
        w = csv.writer(f)
        page_num = 1
        while page_num:
            html = page.inner_html("table")
            soup = BeautifulSoup(html, 'html.parser')
            table = soup
            if table=="None":
                print('OK')
                continue
            if page_num == 1:
                head = table.find("thead")
                items = head.findAll("div", {"class": "L0MOmM"})
                output = []
                for item in items:
                    output.append(item.text)
                w.writerow(output)
            rows = table.findAll("tr", {"class" : "dsil2C"})
            for row in rows:
                items = row.findAll("div", {"class": "tY1czp"})
                if(len(items)==0):
                    continue
                output = []
                for item in items:
                    output.append(item.text)
                w.writerow(output)
            next = page
            page.click('[data-testid=page-next]')
            page.wait_for_load_state("networkidle") 
            sleep(3)
            html = page.inner_html("table")
            newsoup = BeautifulSoup(html, 'html.parser')
            if soup == newsoup:
                break
            page_num = page_num + 1
