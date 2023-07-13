# testing resources --> https://antycaptcha.amberteam.pl

from playwright.sync_api import Playwright, sync_playwright, expect

def test_three_buttons():
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=800)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://antycaptcha.amberteam.pl/exercises/exercise1?seed=3444beaf-6d05-4f65-94f2-c53e87eb28ae")
        page.goto("https://antycaptcha.amberteam.pl/")
        page.get_by_role("link", name="Exercise 1 - Three buttons").click()
        page.get_by_role("button", name="B2").click()
        page.get_by_role("button", name="B2").click()
        page.get_by_role("button", name="B1").click()
        page.get_by_role("button", name="Check solution").click()

    # ---------------------

        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)

    print('Done!')
    
    
    