#https://www.saucedemo.com/

from playwright.sync_api import Playwright, sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    
    #logging process
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    
    #browsing items - lowest price first - adding to a cart
    page.get_by_text("Name (A to Z)Name (A to Z)Name (Z to A)Price (low to high)Price (high to low)").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
    page.locator("#shopping_cart_container a").click()
    
    #removing added item
    page.locator("[data-test=\"remove-sauce-labs-onesie\"]").click()
    page.locator("[data-test=\"continue-shopping\"]").click()
    
    #adding another item - highest price first
    page.get_by_text("Name (A to Z)Name (A to Z)Name (Z to A)Price (low to high)Price (high to low)").click()
    page.locator("[data-test=\"product_sort_container\"]").select_option("hilo")
    page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
    page.locator("#shopping_cart_container a").click()
    
    #checkout process
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("some")
    page.locator("[data-test=\"firstName\"]").press("Tab")
    page.locator("[data-test=\"lastName\"]").fill("name")
    page.locator("[data-test=\"lastName\"]").press("Tab")
    page.locator("[data-test=\"postalCode\"]").fill("dn12jf")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()
    page.locator("[data-test=\"back-to-products\"]").click()
    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="Logout").click()

    # ---------------------
    context.close()
    browser.close()
    print('Thank you for shopping with us')