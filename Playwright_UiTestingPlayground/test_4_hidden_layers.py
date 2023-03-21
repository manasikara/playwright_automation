#http://uitestingplayground.com/hiddenlayers

from playwright.sync_api import sync_playwright


def test_4_hidden_layers():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://uitestingplayground.com")
        page.click('text=Hidden Layers')
        page.click('#greenButton')
        page.click('#blueButton')
        print("you're an amazing automation tester!")
    