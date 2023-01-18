#http://uitestingplayground.com/click

def test_click(page):
    page.goto("http://uitestingplayground.com/")
    page.click('text=Click')
    page.click('#badButton')    
    