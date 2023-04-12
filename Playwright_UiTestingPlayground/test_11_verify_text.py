#http://uitestingplayground.com/verifytext

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('http://uitestingplayground.com/')
    page.click('text=Verify Text')
    welcome_text = page.locator("//span[normalize-space(.)='Welcome UserName!']").text_content()
    print(welcome_text)
    browser.close()
    time.sleep(2)
    print("u're getting better & better, mate!")