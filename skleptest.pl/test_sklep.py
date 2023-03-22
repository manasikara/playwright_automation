from playwright.sync_api import sync_playwright
def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://skleptest.pl/
    page.goto("https://skleptest.pl/")
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
    page.click("text=Return to shop")
    # Images are not being loaded properly!!!
    # assert page.url == "https://skleptest.pl/shop/"
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # assert page.url == "https://skleptest.pl/"
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)


# TOP BAR TESTED - TBC...
