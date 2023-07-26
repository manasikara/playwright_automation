# testing resources --> https://antycaptcha.amberteam.pl

from playwright.sync_api import Playwright, sync_playwright, expect

def test_dropdown():
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=800)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://antycaptcha.amberteam.pl/stf/3-5-2?seed=62415d0f-2f94-46be-bab7-2f1be7c6947b')
        page.click('button.button.u-full-width.off')
        page.get_by_role("button", name="Check solution").click()
        

    # ---------------------

        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)

    print('Done!')
    



        