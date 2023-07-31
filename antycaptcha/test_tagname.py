# testing resources --> https://antycaptcha.amberteam.pl

from playwright.sync_api import Playwright, sync_playwright, expect
import time

def test_tagname():
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=1200)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://antycaptcha.amberteam.pl/stf/3-5-3?seed=e1ec7e75-8cbc-4a99-ad0c-2363640f8be9')
        page.locator('div:has-text("dupa")').click
        

    # ---------------------

        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)

    print('Done!')
    



        