#http://uitestingplayground.com/nbsp

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('http://uitestingplayground.com/')
    page.click('text=Non-Breaking Space')
    page.locator('xpath=My-Button')
    browser.close()
    print('done')
    