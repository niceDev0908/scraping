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
    page.goto('https://www.tutorcircle.hk/case-list.php')
    with open('data.csv','w',newline='',encoding='utf-8-sig') as f:
        w = csv.writer(f)
        while 1:
            html = page.inner_html("article")
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.find("div", {"id": "accordion5"})
            if table=="None":
                print('OK')
                continue
            panels = table.findAll("div", {"class" : "web-design"})
            for panel in panels:
                itemset = panel.find("div", {"class": "row"})
                content = panel.find("div", {"class": "panel-body"})
                items = itemset.findAll("div", {"class": "col-xs-3"})
                if(len(items)==0):
                    continue
                row = []
                for item in items:
                    temp = ""
                    if(item.find("span")):
                        temp = item.text
                    else:
                        temp = temp + item.text
                    row.append(temp)
                content_array = content.findAll("p")
                temp = ""
                for item in content_array:
                    temp = temp + item.text
                
                row.append(temp)
                w.writerow(row)
            next = page
            page.get_by_title('Next page').click()
            page.wait_for_load_state("networkidle") 
            sleep(3)
            html = page.inner_html("article")
            newsoup = BeautifulSoup(html, 'html.parser')
            if soup == newsoup:
                break
