"""
link to view the saved trace --> https://trace.playwright.dev  ,
or locally with a terminal command --> playwright show-trace trace.zip
"""
from playwright.sync_api import sync_playwright, expect
import time
import re
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=600)
    context = browser.new_context()
    page = context.new_page()
    
    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.goto('https://demoqa.com')
    
    # Text box testing
    page.click("(//*[name()='svg'][@stroke='currentColor'])[1]")
    expect(page).to_have_url('https://demoqa.com/elements')
    page.click('span.text')
    page.locator('#userName').fill('Some Name')
    page.locator('#userEmail').fill('someemail@me.com')
    page.locator('#currentAddress').fill('Proin vitae ipsum tincidunt, lacinia nisi pellentesque, ultricies neque.')
    page.locator('#permanentAddress').fill('Proin vitae ipsum tincidunt, lacinia nisi pellentesque, ultricies neque.')
    page.click('#submit')
    
    # Checkbox testing
    
    page.click("text=check box")
    page.click("(//*[name()='svg'][@class='rct-icon rct-icon-expand-close'])[1]")
    page.get_by_role("listitem").filter(has_text=re.compile(r"^Desktop$")).get_by_role("button", name="Toggle").click()
    page.locator("label").filter(has_text="Notes").locator("svg").first.click()
    page.locator("label").filter(has_text="Commands").locator("svg").first.click()
    page.get_by_role("listitem").filter(has_text=re.compile(r"^Downloads$")).get_by_role("button", name="Toggle").click()
    page.locator("label").filter(has_text="Word File.doc").locator("svg").first.click()

    
    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path = "trace.zip")
    
    print('Done! ヽ༼◥▶ل͜◀◤༽ﾉ')
    # ---------------------
    context.close()
    browser.close()

    