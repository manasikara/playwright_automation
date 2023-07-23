# testing resources --> https://antycaptcha.amberteam.pl

from playwright.sync_api import Playwright, sync_playwright, expect
import time

def test_ID():
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=700)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://antycaptcha.amberteam.pl/stf/3-5-1?seed=0049ff84-c450-4e5f-8f66-763b6af0d491")
        page.get_by_test_id('#472c4d6d-3485-4d50-a8dd-3bdc504a06c8').click
        time.sleep(2)

        # ---------------------
        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)
