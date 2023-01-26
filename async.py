from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from time import sleep
import asyncio
import json
import csv
import array


AllEntries = []
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False,slow_mo=50)
        noofforumpagesvodafone = 1000
        currentpage = 1
        page = await browser.new_page()
        await page.goto('https://www.tutorcircle.hk/case-list.php')
        with open('data.csv','w',newline='',encoding='utf-8-sig') as f:
            w = csv.writer(f)
            while 1:
                html = await page.inner_html("div")
                soup = BeautifulSoup(html, 'html.parser')
                table = soup.find("div", {"id": "accordion5"})
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
                await page.get_by_title('Next page').click()
                await page.wait_for_load_state("networkidle") 
asyncio.run(main())

