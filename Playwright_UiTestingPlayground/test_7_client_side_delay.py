#http://uitestingplayground.com/clientdelay

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('http://uitestingplayground.com/')
    page.click('text=Client Side Delay')
    page.click('text=Button Triggering Client Side Logic')
    page.click('text=Data calculated on the client side.')
    print('Done')
