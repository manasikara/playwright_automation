# testing drop-down list

from playwright.sync_api import Playwright, sync_playwright, expect
import re
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://skleptest.pl")
    # Hover over 'catergries' <-- a misspelling BUG here!!! Should be a 'categories' instead.
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()

    # Click "All"
    page.click('text=all')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()

    page.click('text=shirts')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()

    page.click('text=featured')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()

    page.click('text=trends')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()

    page.click('text=scarfs')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()

    page.click('text=shoes')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()

    page.click('text=tops')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()

    page.click('text=blouse')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()

    page.click('text=jeans')
    # Click text=Generic Shop
    page.click("text=Generic Shop")
    # Hover over 'catergries'
    header_menu = page.locator("a.dropdown-toggle", has_text="catergries")
    header_menu.hover()

    page.click('text=dresses')
    # Click text=Generic Shop
    page.click("text=Generic Shop")

    print('Thanks for shopping with us!')
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)






