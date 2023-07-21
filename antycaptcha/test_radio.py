# testing resources --> https://antycaptcha.amberteam.pl

from playwright.sync_api import Playwright, sync_playwright, expect

def test_radio():
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=700)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://antycaptcha.amberteam.pl/exercises/exercise4?seed=9a5ef0b6-a149-4ca5-a875-713ba76f5209")
        page.locator("input:nth-child(6)").first.check()
        page.locator("div:nth-child(5) > input:nth-child(6)").check()
        page.locator("div:nth-child(6) > input").first.check()
        page.locator("div:nth-child(7) > input:nth-child(8)").check()
        page.get_by_role("button", name="Check solution").click()

        # ---------------------
        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)
