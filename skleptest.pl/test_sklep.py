from playwright.sync_api import sync_playwright
import time

# A library which allows to generate random straings. In this case, used to fill-in the comment section
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
    page.click("text=Return to shop") # Images are not being loaded properly!!!
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
    # Click "All"
    # page.select_options('text=All') # <--- STUCK AT DROPDOWN LIST, TBC....
   
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
    # Click text=Jackets For The Soul. What Color Is Yours?
    page.click("text=Jackets For The Soul. What Color Is Yours?")
    # assert page.url == "https://skleptest.pl/jackets-soul-color/"
    # Go to https://skleptest.pl/tag/all/
    page.goto("https://skleptest.pl/tag/all/")
    # Click #recentcomments >> text=Latest Trends For Autumn Are Here!
    page.click("#recentcomments >> text=Latest Trends For Autumn Are Here!")
    # assert page.url == "https://skleptest.pl/latest-trends-autumn/#comment-14"
    # Click textarea[name="comment"]
    page.click("textarea[name=\"comment\"]")
    # Fill textarea[name="comment"]
    page.fill("textarea[name=\"comment\"]", ''.join(random.choices(string.ascii_lowercase, k=5))) # <-- change the comment in each testing attemtp
    # Press Tab
    page.press("textarea[name=\"comment\"]", "Tab")
    # Fill input[name="author"]
    page.fill("input[name=\"author\"]", "me@googlemail.com")
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
    # Click [aria-label="Reply to me@googlemail.com"]
    page.click("[aria-label=\"Reply to me@googlemail.com\"]")
    # Click textarea[name="comment"]
    page.click("textarea[name=\"comment\"]")
    # Fill textarea[name="comment"]
    page.fill("textarea[name=\"comment\"]", "somethig")  # <-- change the comment in each testing attemtp
    # Click text=Post Comment
    page.click("text=Post Comment")
    # assert page.url == "https://skleptest.pl/latest-trends-autumn/#comment-6977"
    # Click #recentcomments >> text=Jackets For The Soul. What Color Is Yours?
    page.click("#recentcomments >> text=Jackets For The Soul. What Color Is Yours?")
    # assert page.url == "https://skleptest.pl/jackets-soul-color/#comment-11"
    # Go to https://skleptest.pl/latest-trends-autumn/#comment-6977
    page.goto("https://skleptest.pl/latest-trends-autumn/#comment-6977")
    # Click text=franek on Jackets For The Soul. What Color Is Yours? >> a
    page.click("text=franek on Jackets For The Soul. What Color Is Yours? >> a")
    # assert page.url == "https://skleptest.pl/jackets-soul-color/#comment-8"
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
    # Click text=Entries RSS
    page.click("text=Entries RSS")
    # assert page.url == "https://skleptest.pl/feed/"
    # Go to https://skleptest.pl/category/fashion/
    page.goto("https://skleptest.pl/category/fashion/")
    # Click text=Comments RSS
    page.click("text=Comments RSS")
    # assert page.url == "https://skleptest.pl/comments/feed/"
    # Go to https://skleptest.pl/category/fashion/
    page.goto("https://skleptest.pl/category/fashion/")
    # Click text=WordPress.org
    page.click("text=WordPress.org")
    # assert page.url == "https://wordpress.org/"
    # Go to https://skleptest.pl/category/fashion/
    page.goto("https://skleptest.pl/category/fashion/")
    # Click #next
    page.click("#next")
    # Click text=Blog
    page.click("text=Blog")
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
    
    # 'div class item' to be tested next time  ------------
    
    
    print('Done!')
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)



