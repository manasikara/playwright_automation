from playwright.sync_api import Playwright, sync_playwright, expect

def test_top_up():
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()



        page.goto("https://demobank.jaktestowac.pl/phone.html")
        page.get_by_role("link", name="doładowanie telefonu").click()
        page.locator("#widget_1_topup_receiver").select_option("501 xxx xxx")
        page.locator("#widget_1_topup_amount").click()
        page.locator("#widget_1_topup_amount").fill("30")
        page.locator("#uniform-widget_1_topup_agreement span").click()
        page.get_by_role("button", name="doładuj telefon").click()
        page.get_by_role("link", name="mój pulpit").click()
    # ---------------------

        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)

    print('Done!')
    
    
    