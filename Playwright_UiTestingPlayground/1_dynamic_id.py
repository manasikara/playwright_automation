#http://uitestingplayground.com/dynamicid

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://uitestingplayground.com/")
    page.click('//*[@id="overview"]/div/div[1]/div[1]/h3/a')
    page.click('text=Button with Dynamic ID')
    browser.close()
    print('Done')

    
