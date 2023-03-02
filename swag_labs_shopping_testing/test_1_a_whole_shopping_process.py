#https://www.saucedemo.com/
#test slowed down by 400ms to see the certain steps as they occur 

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=400)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")

    #logging process
    # Click [data-test="username"]
    page.click("[data-test=\"username\"]")
    # Fill [data-test="username"]
    page.fill("[data-test=\"username\"]", "standard_user")
    # Press Tab
    page.press("[data-test=\"username\"]", "Tab")
    # Fill [data-test="password"]
    page.fill("[data-test=\"password\"]", "secret_sauce")
    # Click [data-test="login-button"]
    page.click("[data-test=\"login-button\"]")
           
    # sort items by name Z-A
    # Click text=Name (A to Z)Name (A to Z)Name (Z to A)Price (low to high)Price (high to low)
    page.click("text=Name (A to Z)Name (A to Z)Name (Z to A)Price (low to high)Price (high to low)")
    # Select za
    page.select_option("[data-test=\"product_sort_container\"]", "za")
    
    # sort items by price high-low
    # Click text=Name (Z to A)Name (A to Z)Name (Z to A)Price (low to high)Price (high to low)
    page.click("text=Name (Z to A)Name (A to Z)Name (Z to A)Price (low to high)Price (high to low)")
    # Select hilo
    page.select_option("[data-test=\"product_sort_container\"]", "hilo")
    
    # add item to the cart
    # Click text=Sauce Labs Fleece Jacket
    page.click("text=Sauce Labs Fleece Jacket")
    # assert page.url == "https://www.saucedemo.com/inventory-item.html?id=5"
    # Click [data-test="add-to-cart-sauce-labs-fleece-jacket"]
    page.click("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]")
    
    # click 'back to broducts'
    # Click [data-test="back-to-products"]
    page.click("[data-test=\"back-to-products\"]")
    
    # add another item to the cart
    # Click [data-test="add-to-cart-sauce-labs-bike-light"]
    page.click("[data-test=\"add-to-cart-sauce-labs-bike-light\"]")
    
    # go to basket
    # Click a:has-text("2")
    page.click("a:has-text(\"2\")")
    
    # remove one item
    # Click [data-test="remove-sauce-labs-fleece-jacket"]
    page.click("[data-test=\"remove-sauce-labs-fleece-jacket\"]")
    
    
    # click the 'echeck out' button and perform check out process
    page.click("text=Checkout")
    # Click [data-test="firstName"]
    page.click("[data-test=\"firstName\"]")
    # Fill [data-test="firstName"]
    page.fill("[data-test=\"firstName\"]", "some")
    # Press Tab
    page.press("[data-test=\"firstName\"]", "Tab")
    # Fill [data-test="lastName"]
    page.fill("[data-test=\"lastName\"]", "name")
    # Press Tab
    page.press("[data-test=\"lastName\"]", "Tab")
    # Fill [data-test="postalCode"]
    page.fill("[data-test=\"postalCode\"]", "dn12jf")
    # Click [data-test="continue"]
    page.click("[data-test=\"continue\"]")
    # Click [data-test="finish"]
    page.click("[data-test=\"finish\"]")
    # Click [data-test="back-to-products"]
    page.click("[data-test=\"back-to-products\"]")
    
    # log out
    # Click text=Open Menu
    page.click("text=Open Menu")
    # Click text=Logout
    page.click("text=Logout")
    
 # ---------------------
    context.close()
    browser.close()
    print('Thank you for shopping with us! ( ͠° ͟ ͜ʖ ͡ ͠°)')