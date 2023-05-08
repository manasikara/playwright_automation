from playwright.sync_api import Playwright, sync_playwright, expect

def test_login():
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

        # ---------------------

        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)

    print('Done!')
    
    
    
    
    
    
    