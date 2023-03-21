from playwright.sync_api import sync_playwright
import time

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False,slomo=400)
    page = browser.new_page()
    page.goto("https://skleptest.pl/")
    # other actions...
    browser.close()

with sync_playwright() as playwright:
    run(playwright)