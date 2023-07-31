# testing resources --> https://antycaptcha.amberteam.pl

from playwright.sync_api import Playwright, sync_playwright, expect
import time

def test_navigate():
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=700)
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://antycaptcha.amberteam.pl/stf/3-2-1/")
        #  ? ? ? ? ? ?? ? ? ? <--- no clue how to do this
        time.sleep(2)

        # ---------------------
        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)

# need to work on this one!!!!!!!