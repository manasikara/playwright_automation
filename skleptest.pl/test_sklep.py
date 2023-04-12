from playwright.sync_api import sync_playwright
import time
# 'random' A library which allows to generate random straings. In this case, used to fill-in the comment section
import random
import string

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    # Go to https://skleptest.pl/
    page.goto("https://skleptest.pl/")
    
    # Top bar testing ------------------
    
    # Click text=skleptestarmy@gmail.com
    page.click("text=skleptestarmy@gmail.com")
    # assert page.url == "https://skleptest.pl/#"
    # Click [placeholder="Search ..."]
    page.click("[placeholder=\"Search ...\"]")
    # Fill [placeholder="Search ..."]
    page.fill("[placeholder=\"Search ...\"]", "dress")
    # Press Enter
    page.press("[placeholder=\"Search ...\"]", "Enter")
    # assert page.url == "https://skleptest.pl/?s=dress"
    # Click text=Account
    page.click("text=Account")
    # assert page.url == "https://skleptest.pl/my-account/"
    # Click text=My Cart - zł 0
    page.click("text=My Cart - zł 0")
    # assert page.url == "https://skleptest.pl/cart/"
    # Click text=Return to shop
    page.click("text=Return to shop") # a BUG <-- Images are not being loaded properly!!!
    # assert page.url == "https://skleptest.pl/shop/"
    # Click text=Generic Shop
    page.click(".site-title")
    
    # Site navigation testing -------------------
    
    # Click "Shop"
    page.click('#menu-item-142')
    # Click "Most Wanted"
    page.click('#menu-item-128')
    # Click "Categories"
    page.click('a.dropdown-toggle')
    
    # Hover over 'catergries' <-- a misspelling BUG here!!! Should be a 'categories' instead.
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()
    
    # Click "All"
    page.click('text=all')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()
    
    page.click('text=shirts')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()
    
    page.click('text=featured')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()
    
    page.click('text=trends')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()
    
    page.click('text=scarfs')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()
    
    page.click('text=shoes')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()
    
    page.click('text=tops')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()
    
    page.click('text=blouse')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()
    
    page.click('text=jeans')
    # Click text=Generic Shop
    page.click("text=Generic Shop")   
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()
    
    page.click('text=dresses')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    
    # Click "About Us"
    page.click('text=about us')
    # Filling-in a "Contact" form
    # Click input[name="your-name"]
    page.click("input[name=\"your-name\"]")
    # Fill input[name="your-name"]
    page.fill("input[name=\"your-name\"]", "some")
    # Press Tab
    page.press("input[name=\"your-name\"]", "Tab")
    # Fill input[name="your-email"]
    page.fill("input[name=\"your-email\"]", "name")
    # Press Tab
    page.press("input[name=\"your-email\"]", "Tab")
    # Fill input[name="your-subject"]
    page.fill("input[name=\"your-subject\"]", ''.join(random.choices(string.ascii_lowercase, k=5)))
    # Click textarea[name="your-message"]
    page.click("textarea[name=\"your-message\"]")
    # Fill textarea[name="your-message"]
    page.fill("textarea[name=\"your-message\"]", ''.join(random.choices(string.ascii_lowercase, k=5)))
    # Click text=Send
    page.click("text=Send")
    
    # Click "Blog"
    # Click text=Blog
    page.click("text=Blog")
    # assert page.url == "https://skleptest.pl/tag/all/"
    # Click [placeholder="Search …"]
    page.click("[placeholder=\"Search …\"]")
    # Fill [placeholder="Search …"]
    page.fill("[placeholder=\"Search …\"]", "dress")
    # Click input:has-text("Search")
    page.click("input:has-text(\"Search\")")
    # assert page.url == "https://skleptest.pl/?s=dress"
    # Go to https://skleptest.pl/tag/all/
    page.goto("https://skleptest.pl/tag/all/")
    # Click text=Search for: Search Search for: Search Recent Posts Best Fabrics For Your Dream D >> [placeholder="Search …"]
    page.click("text=Search for: Search Search for: Search Recent Posts Best Fabrics For Your Dream D >> [placeholder=\"Search …\"]")
    # Fill text=Search for: Search Search for: Search Recent Posts Best Fabrics For Your Dream D >> [placeholder="Search …"]
    page.fill("text=Search for: Search Search for: Search Recent Posts Best Fabrics For Your Dream D >> [placeholder=\"Search …\"]", "dress")
    # Press Enter
    page.press("text=Search for: Search Search for: Search Recent Posts Best Fabrics For Your Dream D >> [placeholder=\"Search …\"]", "Enter")
    # assert page.url == "https://skleptest.pl/?s=dress"
    # Go to https://skleptest.pl/tag/all/
    page.goto("https://skleptest.pl/tag/all/")
    # Click #search-2 [placeholder="Search …"]
    page.click("#search-2 [placeholder=\"Search …\"]")
    # Fill #search-2 [placeholder="Search …"]
    page.fill("#search-2 [placeholder=\"Search …\"]", "dress")
    # Click #search-2 input:has-text("Search")
    page.click("#search-2 input:has-text(\"Search\")")
    # assert page.url == "https://skleptest.pl/?s=dress"
    # Go to https://skleptest.pl/tag/all/
    page.goto("https://skleptest.pl/tag/all/")
    # Click text=Best Fabrics For Your Dream Dress!
    page.click("text=Best Fabrics For Your Dream Dress!")
    # assert page.url == "https://skleptest.pl/best-fabrics-dream-dress-dare-try/"
    # Go to https://skleptest.pl/tag/all/
    page.goto("https://skleptest.pl/tag/all/")
    # Click text=Latest Trends For Autumn Are Here!
    page.click("text=Latest Trends For Autumn Are Here!")
    # assert page.url == "https://skleptest.pl/latest-trends-autumn/"
    # Go to https://skleptest.pl/tag/all/
    page.goto("https://skleptest.pl/tag/all/")
    # Click text=Long Legs? No Longer A Myth! Check it out!
    page.click("text=Long Legs? No Longer A Myth! Check it out!")
    # assert page.url == "https://skleptest.pl/long-legs-no-longer-myth-check/"
    # Go to https://skleptest.pl/tag/all/
    page.goto("https://skleptest.pl/tag/all/")
    time.sleep(1)
    # Click text=Jackets For The Soul. What Color Is Yours?
    page.click("text=Jackets For The Soul. What Color Is Yours?")
    # assert page.url == "https://skleptest.pl/jackets-soul-color/"
    
    # Testing the 'Recent Comments' div
    
    # Go to https://skleptest.pl/tag/all/
    page.goto("https://skleptest.pl/tag/all/")
    # Click #recentcomments >> text=Latest Trends For Autumn Are Here!
    page.click("//body/div[@id='page']/div[@class='site-content']/div[@class='container']/div[@class='row']/aside[@id='secondary']/div[@id='recent-comments-2']/ul[@id='recentcomments']/li[1]/a[1]")
    # assert page.url == "https://skleptest.pl/latest-trends-autumn/#comment-14"
    # Click textarea[name="comment"]
    page.click("textarea[name=\"comment\"]")
    # Fill textarea[name="comment"]
    page.fill("textarea[name=\"comment\"]", ''.join(random.choices(string.ascii_lowercase, k=50))) 
    # Press Tab
    page.press("textarea[name=\"comment\"]", "Tab")
    # Fill input[name="author"]
    page.fill("input[name=\"author\"]", ''.join(random.choices(string.ascii_lowercase, k=7))) 
    # Press Tab
    page.press("input[name=\"author\"]", "Tab")
    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "me@googlemail.com")
    # Press Tab
    page.press("input[name=\"email\"]", "Tab")
    # Fill input[name="url"]
    page.fill("input[name=\"url\"]", "somewebsite.com")
    # Click text=Post Comment
    page.click("text=Post Comment")
    # assert page.url == "https://skleptest.pl/latest-trends-autumn/#comment-6976"
    
    # Click text=September 2017
    page.click("text=September 2017")
    # assert page.url == "https://skleptest.pl/2017/09/"
    # Click text=June 2017
    page.click("text=June 2017")
    # assert page.url == "https://skleptest.pl/2017/06/"
    # Click text=March 2017
    page.click("text=March 2017")
    # assert page.url == "https://skleptest.pl/2017/03/"
    # Click text=Fashion
    page.click("text=Fashion")
    # assert page.url == "https://skleptest.pl/category/fashion/"
    # Click text=Log in
    page.click("text=Log in")
    # assert page.url == "https://skleptest.pl/wp-login.php"
    # Go to https://skleptest.pl/category/fashion/
    page.goto("https://skleptest.pl/category/fashion/")
   
    # Click text=WordPress.org
    page.click("text=WordPress.org")
    # assert page.url == "https://wordpress.org/"
    # Go to https://skleptest.pl/category/fashion/
    page.goto("https://skleptest.pl/category/fashion/")
    # assert page.url == "https://skleptest.pl/tag/all/"
    # Click [placeholder="Search …"]
    page.click("[placeholder=\"Search …\"]")
    # Fill [placeholder="Search …"]
    page.fill("[placeholder=\"Search …\"]", "blog")
    # Press Enter
    page.press("[placeholder=\"Search …\"]", "Enter")
    # assert page.url == "https://skleptest.pl/?s=blog"
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # assert page.url == "https://skleptest.pl/"
    
    # Testing div class 'item'
    
    page.click("//div[@class='owl-item active']//a[normalize-space()='Shop Now']") #  <-- Website crashes at this point
    # Go to https://skleptest.pl/
    page.goto("https://skleptest.pl/")
    # Click :nth-match(:text("Learn More"), 3)
    page.click(":nth-match(:text(\"Learn More\"), 3)")
    # Go to https://skleptest.pl/
    page.goto("https://skleptest.pl/")
    
    # Testing div class 'site-content'
    # Adding all the available items to the cart
    
    # Click text=Add to cart
    page.click("text=Add to cart") # a BUG!!! <-- image missing!!!
    # Click #tyche_products-1 >> :nth-match(:text("Add to cart"), 2)
    page.click("#tyche_products-1 >> :nth-match(:text(\"Add to cart\"), 2)")
    # Click #tyche_products-1 >> :nth-match(:text("Add to cart"), 3)
    page.click("#tyche_products-1 >> :nth-match(:text(\"Add to cart\"), 3)")
    # Click text=BUY NOW
    page.click("text=BUY NOW")
    # assert page.url == "https://skleptest.pl/skleptest.pl/?s="
    # Go to https://skleptest.pl/
    page.goto("https://skleptest.pl/")
    # Click #tyche_products-2 >> text=BUY NOW
    page.click("#tyche_products-2 >> text=BUY NOW")
    # assert page.url == "https://skleptest.pl/skleptest.pl/?s="
    # Go to https://skleptest.pl/
    page.goto("https://skleptest.pl/")
    # Click #tyche_products-2 >> text=Add to cart
    page.click("#tyche_products-2 >> text=Add to cart")
    # Click text=Manago Shirt Rated 5.00 out of 5 25 zł Add to cart >> :nth-match(a, 2)
    page.click("text=Manago Shirt Rated 5.00 out of 5 25 zł Add to cart >> :nth-match(a, 2)")
    # Click text=Blue Sweater Rated 4.00 out of 5 25 zł 15 zł Add to cart >> :nth-match(a, 2)
    page.click("text=Blue Sweater Rated 4.00 out of 5 25 zł 15 zł Add to cart >> :nth-match(a, 2)")
    # Click #tyche_products-3 >> text=Add to cart
    page.click("#tyche_products-3 >> text=Add to cart")
    # Click #tyche_products-4 >> text=Add to cart
    page.click("#tyche_products-4 >> text=Add to cart")
    # Click #tyche_products-5 >> text=Add to cart
    page.click("#tyche_products-5 >> text=Add to cart")
    # Click #tyche_products-3 >> :nth-match(:text("Add to cart"), 2)
    page.click("#tyche_products-3 >> :nth-match(:text(\"Add to cart\"), 2)")
    # Click #tyche_products-4 >> :nth-match(:text("Add to cart"), 2)
    page.click("#tyche_products-4 >> :nth-match(:text(\"Add to cart\"), 2)")
    # Click #tyche_products-5 >> :nth-match(:text("Add to cart"), 2)
    page.click("#tyche_products-5 >> :nth-match(:text(\"Add to cart\"), 2)")
    # Click #tyche_products-3 >> :nth-match(:text("Add to cart"), 3)
    page.click("#tyche_products-3 >> :nth-match(:text(\"Add to cart\"), 3)")
    # Click #tyche_products-4 >> :nth-match(:text("Add to cart"), 3)
    page.click("#tyche_products-4 >> :nth-match(:text(\"Add to cart\"), 3)")
    # Click #tyche_products-5 >> :nth-match(:text("Add to cart"), 3)
    page.click("#tyche_products-5 >> :nth-match(:text(\"Add to cart\"), 3)")
    # Click #tyche_products-6 >> text=Add to cart
    page.click("#tyche_products-6 >> text=Add to cart")
    # Click #tyche_products-6 >> :nth-match(:text("Add to cart"), 2)
    page.click("#tyche_products-6 >> :nth-match(:text(\"Add to cart\"), 2)")
    # Click #tyche_products-6 >> :nth-match(:text("Add to cart"), 3)
    page.click("#tyche_products-6 >> :nth-match(:text(\"Add to cart\"), 3)")
    # Click #tyche_products-6 >> :nth-match(:text("Add to cart"), 4)
    page.click("#tyche_products-6 >> :nth-match(:text(\"Add to cart\"), 4)")
    # Click #tyche_products-7 >> text=Add to cart
    page.click("#tyche_products-7 >> text=Add to cart")
    # Click #tyche_products-7 >> :nth-match(:text("Add to cart"), 2)
    page.click("#tyche_products-7 >> :nth-match(:text(\"Add to cart\"), 2)")
    # Click #tyche_products-7 >> :nth-match(:text("Add to cart"), 3)
    page.click("#tyche_products-7 >> :nth-match(:text(\"Add to cart\"), 3)")
    # Click #tyche_products-7 >> :nth-match(:text("Add to cart"), 4)
    page.click("#tyche_products-7 >> :nth-match(:text(\"Add to cart\"), 4)")
    time.sleep(2)
    # Click text=My Cart - zł 0
    page.click("text=My Cart - zł 40") # a BUG!!! <-- The cart shows a wrong ammount
    # assert page.url == "https://skleptest.pl/cart/"
    
    # Removing items singly from the cart list
    
    # Click text=×
    page.click("text=×") # a BUG!!! <-- can't remove the items 
    
    #Applying the coupon code
    # Click [placeholder="Coupon code"]
    page.click("[placeholder=\"Coupon code\"]")
    # Fill [placeholder="Coupon code"]
    page.fill("[placeholder=\"Coupon code\"]", "asdf1234")
    # Click text=Apply coupon
    page.click("text=Apply coupon") # a BUG!!! <-- can't appyly a coupon code
    # Click text=Proceed to checkout
    page.click("text=Proceed to checkout")
    # Click input[name="billing_first_name"]
    page.click("input[name=\"billing_first_name\"]")
    # Fill input[name="billing_first_name"]
    page.fill("input[name=\"billing_first_name\"]", "some")
    # Press Tab
    page.press("input[name=\"billing_first_name\"]", "Tab")
    # Fill input[name="billing_last_name"]
    page.fill("input[name=\"billing_last_name\"]", "name")
    # Press Tab
    page.press("input[name=\"billing_last_name\"]", "Tab")
    # Fill input[name="billing_company"]
    page.fill("input[name=\"billing_company\"]", "xxx")
    # Click span[role="textbox"]:has-text("Poland")
    page.click("span[role=\"textbox\"]:has-text(\"Poland\")")
    # Click li[role="option"]:has-text("United Kingdom (UK)")
    page.click("li[role=\"option\"]:has-text(\"United Kingdom (UK)\")")
    # 0× click
    page.click("text=County")
    # Click [placeholder="House number and street name"]
    page.click("[placeholder=\"House number and street name\"]")
    # Fill [placeholder="House number and street name"]
    page.fill("[placeholder=\"House number and street name\"]", "81 Hindhead Road")
    # Click input[name="billing_city"]
    page.click("input[name=\"billing_city\"]")
    # Fill input[name="billing_city"]
    page.fill("input[name=\"billing_city\"]", "Earl Soham")
    # Click input[name="billing_postcode"]
    page.click("input[name=\"billing_postcode\"]")
    # Fill input[name="billing_postcode"]
    page.fill("input[name=\"billing_postcode\"]", "IP13 1JX")
    # 0× click
    page.click("text=Home /Shop/Checkout Checkout Returning customer? Click here to login If you have")
    # Click input[name="billing_phone"]
    page.click("input[name=\"billing_phone\"]", modifiers=["Control"])
    # Fill input[name="billing_phone"]
    page.fill("input[name=\"billing_phone\"]", "070 2135 8078")
    # Click input[name="billing_email"]
    page.click("input[name=\"billing_email\"]")
    # Fill input[name="billing_email"]
    page.fill("input[name=\"billing_email\"]", "me@googlemail.com")
    time.sleep(2)
    # Click text=Place order
    # with page.expect_navigation(url="https://skleptest.pl/checkout/order-received/5082/?key=wc_order_642568013da28"):
    with page.expect_navigation():
        page.click("text=Place order")
    time.sleep(3)    
    
    # Saving the order details
    page.screenshot(path="screenshot.png")
    
    
    print('Thanks for shopping with us!')
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)



