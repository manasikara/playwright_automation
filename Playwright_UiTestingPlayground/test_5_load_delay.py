#http://uitestingplayground.com/loaddelay

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('http://uitestingplayground.com/')
    page.click('text=Load Delay')
    page.click('button.btn-primary')
    page.close()
    print('Success!')
    