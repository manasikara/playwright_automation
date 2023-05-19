# https://www.demoblaze.com/index.html

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.demoblaze.com/index.html")
    page.get_by_role("link", name="Log in").click()
    page.locator("#loginusername").click()
    page.locator("#loginusername").fill("slawek")
    page.locator("#loginusername").press("Tab")
    page.locator("#loginpassword").fill("123123123")
    page.get_by_role("button", name="Log in").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
