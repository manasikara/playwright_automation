# testing resources --> https://antycaptcha.amberteam.pl

from playwright.sync_api import Playwright, sync_playwright, expect

def test_three_buttons():
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=800)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://antycaptcha.amberteam.pl/exercises/exercise3?seed=89c22dde-2af2-4041-af81-185afd93dd85")
        page.get_by_role("combobox").select_option("v6")
        page.get_by_role("button", name="Check solution").click()
        

    # ---------------------

        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)

    print('Done!')
    



        