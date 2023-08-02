# testing resources --> https://antycaptcha.amberteam.pl

from playwright.sync_api import Playwright, sync_playwright, expect


def test_alert():
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=800)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://antycaptcha.amberteam.pl/stf/3-8-1?seed=9f718e18-945e-49ee-bd36-f6691aa5706d")
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.get_by_role("button", name="Alert").click()
        page.locator("#alertText").click()
        page.locator("#alertText").fill("Lose myself usually official seem read first.")
        page.get_by_role("button", name="Check solution").click()


        # ---------------------

        context.close()
        browser.close()

    with sync_playwright() as playwright:
        run(playwright)

    print('Done!')
    





