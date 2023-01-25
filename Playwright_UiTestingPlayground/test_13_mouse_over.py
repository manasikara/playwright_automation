#http://uitestingplayground.com/mouseover

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://uitestingplayground.com/mouseover")
    page.get_by_text("Click me").click()
    page.get_by_text("Click me").click()
    page.get_by_text("Click me").click()
    page.get_by_text("Click me").click()
    page.get_by_text("Click me").click()
    page.get_by_text("Click me").click()
    page.get_by_text("Click me").click()
    page.get_by_text("Click me").click()

    time.sleep(2)
    page.screenshot(path="screenshot.png")
    print("The link clicked 8 times - see screenshot")
    browser.close()