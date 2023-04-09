# website tested --> https://demoqa.com/

from playwright.sync_api import sync_playwright, expect
import time
import re


def test_elements():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto('https://demoqa.com/elements')
    
        # Text box testing
        
        page.click('span.text')
        page.locator('#userName').fill('Some Name')
        page.locator('#userEmail').fill('someemail@me.com')
        page.locator('#currentAddress').fill('Proin vitae ipsum tincidunt, lacinia nisi pellentesque,   ultricies neque.')
        page.locator('#permanentAddress').fill('Proin vitae ipsum tincidunt, lacinia nisi pellentesque, ultricies neque.')
        page.click('#submit')

        # Checkbox

        page.click("text=check box")
        page.click("(//*[name()='svg'][@class='rct-icon rct-icon-expand-close'])[1]")
        page.get_by_role("listitem").filter(has_text=re.compile(r"^Desktop$")).get_by_role("button",name="Toggle").click()
        page.locator("label").filter(has_text="Notes").locator("svg").first.click()
        page.locator("label").filter(has_text="Commands").locator("svg").first.click()
        page.get_by_role("listitem").filter(has_text=re.compile(r"^Downloads$")).get_by_role("button",name="Toggle").click()
        page.locator("label").filter(has_text="Word File.doc").locator("svg").first.click()
        page.click('text=radio button')

        # Radio Button
        
        page.click("label[for='yesRadio']")
        page.click("label[for='impressiveRadio']")
    
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
        page.click(".-totalPages")
        page.get_by_role("spinbutton", name="jump to page").press("Tab")
        page.get_by_role("combobox", name="rows per page").press("Enter")
        page.get_by_role("combobox", name="rows per page").select_option("10")
        keyboard = page.keyboard
        keyboard.press('Enter')
        
        
        # Buttons
        
        page.goto("https://demoqa.com/buttons")
        page.get_by_text("Double Click Me").dblclick()
        page.get_by_text("Right Click Me").click(button="right")
        page.get_by_title("Click Me")
        
        # Links
        
        page.click("(//li[@id='item-5'])[1]")
        with page.expect_popup() as page1_info:
            page.get_by_role("link", name="Home", exact=True).click()
            page1 = page1_info.value
            page1.close()
        with page.expect_popup() as page2_info:
            page.click("#dynamicLink")
            page2 = page2_info.value
            page2.close()
            
        page.click("#created")
        page.click("#no-content")
        page.click("#moved")
        page.click("#bad-request")
        page.click("#unauthorized")
        page.click("#forbidden")
        page.click("#invalid-url")                
        
        # Broken Links/Images
        
        page.click("text=Broken Links - Images")     
        page.get_by_role("img").nth(2).click()
        page.get_by_role("img").nth(3).click()
        page.get_by_role("link", name="Click Here for Valid Link").click()
        page.goto("https://demoqa.com/broken")
        page.get_by_role("link", name="Click Here for Broken Link").click()
        page.goto("https://demoqa.com/broken")
        
        # Upload and Download
        
        page.click("text=Upload and Download")
        page.click("#downloadButton")
        with page.expect_file_chooser() as fc_info:
            page.click("#uploadFile")
        file_chooser = fc_info.value
        file_chooser.set_files("sampleFile.jpeg")
        
        # Dynamic Propeties
        
        page.click("text=Dynamic Properties")
        page.click("text=Will enable 5 seconds")
        page.click("#colorChange")
        page.click("#visibleAfter")
        
        # Forms 
        page.click("text=Forms")
        page.click("text=Practice Form")
        page.get_by_role("textbox", name="First Name").fill("some")
        page.get_by_role("textbox", name="Last Name").fill("name")
        page.get_by_role("textbox", name="name@example.com").fill("some_email@gmail.com")
        page.get_by_text("Male", exact=True).click()
        page.get_by_text("Female", exact=True).click()
        page.get_by_text("Other", exact=True).click()
        page.get_by_role("textbox", name="Mobile Number").fill("123123123")
        page.locator("#dateOfBirthInput").fill("01.04.1978")
        page.locator("body").press("Tab")
        page.locator("#subjectsInput").fill("some subject here")
        page.get_by_text("Sports", exact=True).click()
        page.get_by_text("Reading", exact=True).click()
        page.get_by_text("Music", exact=True).click()
        with page.expect_file_chooser() as fc_info:
            page.click("#uploadPicture")
        file_chooser = fc_info.value
        file_chooser.set_files("sampleFile.jpeg")
        page.get_by_role("textbox", name="Current Address").fill("some address")
        page.get_by_text("Select State").click()
        page.get_by_text("NCR", exact=True).click()
        page.get_by_text("Select City").click()
        page.get_by_text("Delhi", exact=True).click()
        
        # Alerts, Frames & Windows
        # Browser Windows
        
        page.click("text=Alerts, Frame & Windows")
        page.click("text=Browser Windows")
        with page.expect_popup() as page1_info:
            page.get_by_role("button", name="New Tab").click()
        page1 = page1_info.value
        page1.close()
        with page.expect_popup() as page2_info:
            page.get_by_role("button", name="New Window", exact=True).click()
        page2 = page2_info.value
        page2.close()
        with page.expect_popup() as page3_info:
            page.get_by_role("button", name="New Window Message").click()
        page3 = page3_info.value
        page3.close()
        
        # Alerts
        page.goto("https://demoqa.com/alerts")
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.locator("#alertButton").click()
        page.locator("#timerAlertButton").click()
        page.get_by_role("link").click()
        page.goto("https://demoqa.com/alerts")
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.locator("#confirmButton").click()
        click_js_button = page.locator("//button[@id='promtButton']")
        page.on("dialog", lambda dialog: dialog.accept(prompt_text='some text'))
        click_js_button.click()        
        
        
        
        browser.close()
        print('Done! ᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿) ᕗ')
        
        # to be continued ! ! !......... "frames" next




