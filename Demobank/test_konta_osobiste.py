from playwright.sync_api import Playwright, sync_playwright, expect

def test_konta_osobiste():
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
        
        # Konta osobiste
        page.get_by_role("link", name="konta osobiste").click()
        page.get_by_role("link", name="historia konta").click()
        page.get_by_role("link", name="szczegóły konta").click()
        page.get_by_role("link", name="szczegóły »").click()
        page.get_by_role("link", name="wykonaj przelew").click()
        page.get_by_role("link", name="mój pulpit").click()
        
        
        # ---------------------

        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)

    print('Done!')