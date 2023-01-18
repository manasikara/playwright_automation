#learning automation using a pytest
#http://uitestingplayground.com/classattr
#https://playwright.dev/python/docs/test-runners

def test_class_attribute(page)
    page.goto("http://uitestingplayground.com/")
    page.click('//*[@id="overview"]/div/div[1]/div[2]/h3/a')
    page.click(":button('.btn class1 btn-success btn-test')")
    
    
    
    