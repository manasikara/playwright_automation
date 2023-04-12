# site tested --> https://automationteststore.com/

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False, slow_mo=600)
    page = browser.new_page()
    page.goto('https://www.automationteststore.com')
    
    # currency change
    page.locator("a").filter(has_text="$ US Dollar").first.click()
    page.get_by_role("link", name="€ Euro").click()
    
    # keyword search
    page.get_by_placeholder("Search Keywords").fill("shampoo")
    page.get_by_placeholder("Search Keywords").press("Enter")
    
    # sorting by price
    page.locator("#sort").select_option("p.price-DESC")
    page.locator("div:nth-child(2) > .thumbnail > a").click()
    
    # reading reviews
    page.get_by_role("link", name="Reviews (1)").click()
    
    # adding desired quantity to the cart
    page.locator("#product_quantity").click()
    page.locator("#product_quantity").fill("5")
    page.get_by_role("link", name=" Add to Cart").click()
    
    # cart update
    page.locator("#cart_quantity74").click()
    page.locator("#cart_quantity74").fill("2")
    page.get_by_role("button", name=" Update").click()
   
    # entering and applying coupon code
    page.locator("#coupon_coupon").fill("54321")
    page.get_by_role("button", name=" Apply Coupon").click()
    
    # generating the estimate shipping fee
    page.locator("#estimate_country").select_option("170")
    page.locator("#estimate_country_zones").select_option("2642")
    page.locator("#estimate_postcode").click()
    page.locator("#estimate_postcode").fill("41-933")
    page.get_by_role("button", name=" Estimate").click()
    
    # checking-out
    page.locator("#cart_checkout2").click()
    page.get_by_text("Guest Checkout").click()
    page.get_by_role("button", name=" Continue").click()
    page.locator("#guestFrm_firstname").click()
    page.locator("#guestFrm_firstname").fill("Some")
    page.locator("#guestFrm_firstname").press("Tab")
    page.locator("#guestFrm_lastname").fill("Name")
    page.locator("#guestFrm_email").click()
    page.locator("#guestFrm_email").fill("someEmail@googlemail.com")
    page.locator("#guestFrm_telephone").click()
    page.locator("#guestFrm_telephone").fill("34789 789")
    page.locator("#guestFrm_address_1").click()
    page.locator("#guestFrm_address_1").fill("some")
    page.locator("#guestFrm_address_1").press("Tab")
    page.locator("#guestFrm_address_2").fill("address")
    page.locator("#guestFrm_address_2").press("Tab")
    page.locator("#guestFrm_city").fill("some city")
    page.locator("#guestFrm_zone_id").select_option("3522")
    page.locator("#guestFrm_postcode").click()
    page.locator("#guestFrm_postcode").click()
    page.locator("#guestFrm_postcode").fill("06010 ")
    page.get_by_role("button", name=" Continue").click()
    
    # editing a payment
    page.get_by_role("link", name=" Edit Payment").click()
    page.locator("#guest_comment").click()
    page.locator("#guest_comment").fill("no comments")
    page.get_by_label("I have read and agree to the Return Policy").check()
    page.get_by_role("button", name=" Continue").click()
    page.get_by_role("button", name=" Confirm Order").click()
    page.get_by_role("link", name=" Continue").click()
    
    
    browser.close()
    print("All good ᕦ(ò_óˇ)")