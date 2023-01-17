#http://uitestingplayground.com/classattr

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://uitestingplayground.com/")
    page.click('//*[@id="overview"]/div/div[1]/div[2]/h3/a')
    
    
    print("congrats, u're amazing automation tester!")
