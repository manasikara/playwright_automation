#http://uitestingplayground.com/hiddenlayers
#headless test

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://uitestingplayground.com")
    page.click('text=Hidden Layers')
    page.click('#greenButton')
    page.click('#blueButton')
    print("you're an amazing automation tester!")
    