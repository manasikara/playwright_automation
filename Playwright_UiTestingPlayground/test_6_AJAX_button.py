#http://uitestingplayground.com/ajax

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('http://uitestingplayground.com/')
    page.click('text=AJAX Data')
    page.click('button#ajaxButton')
    time.sleep(17)
    page.click('text = Data loaded with AJAX get request.')
    page.close()
    print('AJAX text appeared')
    