#http://uitestingplayground.com/overlapped

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('http://uitestingplayground.com/')
    page.click('text=Overlapped Element')
    page.get_by_placeholder('id').fill('123123123')
    time.sleep(2)
    page.locator('#name').fill('some name')
    time.sleep(2)
    page.get_by_placeholder('Subject').fill('_something')
    time.sleep(2)
    browser.close()
    print('done')