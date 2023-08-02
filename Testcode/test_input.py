# website tested --> https://letcode.in/test

from playwright.sync_api import Playwright, sync_playwright, expect

def test_input():
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=700)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://letcode.in/edit")
        page.get_by_placeholder("Enter first & last name").click()
        page.get_by_placeholder("Enter first & last name").fill("Slawomir Tatinger")
        page.locator("#join").click()
        page.locator("#join").fill("something")
        page.locator("#join").press("Tab")

        # ---------------------
        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)

# to be continued....