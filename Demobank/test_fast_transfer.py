from playwright.sync_api import Playwright, sync_playwright, expect


def test_fast_transfer():
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demobank.jaktestowac.pl/")
        page.goto("https://demobank.jaktestowac.pl/logowanie_etap_1.html")
        page.locator("#login_id").click()
        page.locator("#login_id").fill("12345678")
        page.locator("#login_id").press("Enter")
        page.locator("#login_password").click()
        page.locator("#login_password").fill("12345678")
        page.locator("#login_password").press("Enter")

        # Fast transfer
        page.get_by_role("link", name="szybki przelew").click()
        page.locator("#widget_1_transfer_receiver").select_option("2")
        page.locator("#widget_1_transfer_amount").click()
        page.locator("#widget_1_transfer_amount").fill("20,00")
        page.locator("#widget_1_transfer_title").click()
        page.locator("#widget_1_transfer_title").fill("demo transfer")
        page.get_by_role("button", name="wykonaj").click()
        page.get_by_role("link", name="mój pulpit").click()



        # ---------------------

        context.close()
        browser.close()

    with sync_playwright() as playwright:
        run(playwright)

    print('Done!')