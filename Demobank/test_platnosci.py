from playwright.sync_api import Playwright, sync_playwright, expect

def test_platnosci():
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
        keyboard = page.keyboard
        keyboard.press('Enter')
        
        # Płatności
        page.get_by_role("link", name="płatności").click()
        page.locator(".nav-tabs").click()
        page.get_by_placeholder("wpisz nazwę odbiorcy przelewu lub wybierz z listy").click()
        page.get_by_placeholder("wpisz nazwę odbiorcy przelewu lub wybierz z listy").fill("someone")
        page.get_by_placeholder("wpisz nazwę odbiorcy przelewu lub wybierz z listy").press("Tab")
        page.get_by_placeholder("__ ____ ____ ____ ____ ____ ____").fill("12 3456 7890 0000 0000 0000 00000")
        page.locator(".i-show").first.click()
        page.get_by_placeholder("ulica i numer domu / mieszkania").click()
        page.get_by_placeholder("ulica i numer domu / mieszkania").fill("some street and number")
        page.get_by_placeholder("ulica i numer domu / mieszkania").press("Tab")
        page.get_by_placeholder("kod pocztowy, miejscowość").fill("23-555")
        page.get_by_placeholder("kod pocztowy, miejscowość").press("Tab")
        page.get_by_placeholder("adres - trzecia linia").fill("222")
        page.get_by_placeholder("adres - trzecia linia").press("Tab")
        page.locator("#form_amount").fill("10")
        page.get_by_text("przelew środków").click()
        page.get_by_text("przelew środków").fill("some title")
        page.locator("#form_ico_calendar").click()
        page.locator("#form_date").click()
        page.get_by_role("link", name="16").click()
        page.locator("#uniform-form_is_email span").click()
        page.locator("#form_email").click()
        page.locator("#form_email").fill("someone@gmail.com")
        page.locator("#uniform-form_add_receiver span").click()
        page.locator("#form_receiver_name").dblclick()
        page.locator("#form_receiver_name").fill("someone else")
        page.get_by_label("jako zaufanego").check()
        page.get_by_role("link", name="dalej").click()
            
        
        
        # ---------------------

        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)

    print('Done!')