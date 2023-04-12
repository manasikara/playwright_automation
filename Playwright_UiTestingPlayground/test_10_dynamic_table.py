#http://uitestingplayground.com/dynamictable

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('http://uitestingplayground.com/')
    page.click('text=Dynamic Table')
    bg_warning = page.locator('.bg-warning').text_content()
    print(bg_warning)
    time.sleep(3)
    page.close()
    print('U did it!')
