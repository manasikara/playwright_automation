#http://uitestingplayground.com/sampleapp
#tested using playwright codegen

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('http://uitestingplayground.com/')
    page.get_by_role("link", name="Sample App").click()
    page.get_by_placeholder("User Name").click()
    page.get_by_placeholder("User Name").fill("appusername")
    page.get_by_placeholder("********").click()
    page.get_by_placeholder("********").fill("pwd")
    page.get_by_role("button", name="Log In").click()
    time.sleep(2)
    page.close()
    print('Done')
    
    
    
