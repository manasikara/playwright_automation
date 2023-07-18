# testing resources --> https://antycaptcha.amberteam.pl

from playwright.sync_api import Playwright, sync_playwright, expect

def test_three_buttons():
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=800)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://antycaptcha.amberteam.pl/exercises/exercise2?seed=9af17c5b-0d85-4922-9b1d-ff1abd7e170b")
        page.get_by_role("textbox").click()
        page.get_by_role("textbox").fill("Cut my coach.")
        page.get_by_role("button", name="B1").click()
        page.get_by_role("button", name="Check solution").click()

    # ---------------------

        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)

    print('Done!')
    


        