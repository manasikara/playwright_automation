# website tested --> https://demoqa.com/

from playwright.sync_api import sync_playwright, expect
import time
import re

def test_elements():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        page = browser.new_page()
        page.goto('https://demoqa.com')

        # Text box testing
        page.click("(//*[name()='svg'][@stroke='currentColor'])[1]")
        expect(page).to_have_url('https://demoqa.com/elements')
        '''
        page.click('span.text')
        page.locator('#userName').fill('Some Name')
        page.locator('#userEmail').fill('someemail@me.com')
        page.locator('#currentAddress').fill('Proin vitae ipsum tincidunt, lacinia nisi pellentesque,   ultricies neque.')
        page.locator('#permanentAddress').fill(
            'Proin vitae ipsum tincidunt, lacinia nisi pellentesque, ultricies neque.')
        page.click('#submit')

        # Checkbox

        page.click("text=check box")
        page.click("(//*[name()='svg'][@class='rct-icon rct-icon-expand-close'])[1]")
        page.get_by_role("listitem").filter(has_text=re.compile(r"^Desktop$")).get_by_role("button",
                                                                                           name="Toggle").click()
        page.locator("label").filter(has_text="Notes").locator("svg").first.click()
        page.locator("label").filter(has_text="Commands").locator("svg").first.click()
        page.get_by_role("listitem").filter(has_text=re.compile(r"^Downloads$")).get_by_role("button",
                                                                                             name="Toggle").click()
        page.locator("label").filter(has_text="Word File.doc").locator("svg").first.click()
        page.click('text=radio button')

        # Radio Button
        page.click("label[for='yesRadio']")
        page.click("label[for='impressiveRadio']")
        '''
        # Web Tables
        page.click('text=Web Tables')
        page.click("text=First Name")
        page.click("text=Last Name")
        page.click("//div[contains(text(),'Age')]")
        page.click("text=Email")
        page.click("text=Salary")
        page.click("text=Department")
        page.click("text=Action")
        page.click("(//*[name()='path'])[54]")
        page.get_by_placeholder("First Name").click()
        page.get_by_placeholder("First Name").fill("some")
        page.get_by_placeholder("First Name").press("Tab")
        page.get_by_placeholder("Last Name").fill("name")
        page.get_by_placeholder("Last Name").press("Tab")
        page.get_by_placeholder("name@example.com").fill("someemail@gmail.com")
        page.get_by_placeholder("name@example.com").press("Tab")
        page.get_by_placeholder("Age").fill("43")
        page.get_by_placeholder("Age").press("Tab")
        page.get_by_placeholder("Salary").fill("20000")
        page.get_by_placeholder("Salary").press("Tab")
        page.get_by_placeholder("Department").fill("IT")
        page.get_by_role("button", name="Submit").click()
        page.click("(//*[name()='path'])[55]")
        page.click("(//*[name()='path'])[57]")
        page.locator(".select-wrap -pageSizeOptions").click()


        print('Done! ᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿) ᕗ')
        # ---------------------
        browser.close()


# to be continued............!!!


