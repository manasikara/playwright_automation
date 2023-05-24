from playwright.sync_api import Playwright, sync_playwright, expect
import time

def test_p_form():
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=600)
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://www.seleniumframework.com/Practiceform/")
        with page.expect_popup() as page1_info:
            page.get_by_role("button", name="New Browser Window").click()
        page1 = page1_info.value
        page1.close()
        with page.expect_popup() as page2_info:
            page.get_by_role("button", name="New Message Window").click()
        page2 = page2_info.value
        page2.close()
        with page.expect_popup() as page3_info:
            page.get_by_role("button", name="New Browser Tab").click()
        page3 = page3_info.value
        page3.close()
        page.get_by_text("Find me I have nothing in me!!").click()
        page.get_by_text("I will have random ID").click()

        page.click("text=Alert Box")
        page.get_by_role("button", name="Alert Box").click()



        print('Done!')
        # ---------------------
        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)
