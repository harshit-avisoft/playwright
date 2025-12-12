from playwright.sync_api import Page,expect

def test_broken_links(page:Page):
    page.goto("https://demoqa.com/broken")
    expect(page).to_have_url("https://demoqa.com/broken")

    # page.get_by_text("Click Here for Valid Link").click()
    # page.locator('a[href="http://demoqa.com"]').click()
    # expect(page).to_have_url("https://demoqa.com/")

    # page.locator("div > a:nth-of-type(1)").click() there are 3 matches so this will not work
    # page.locator("div > a").nth(0).hover() there are many a in many div so this is not working
    # page.locator("a").nth(0).click() same case as above
    page.get_by_text("Click Here for Broken Link").click()
    expect(page).to_have_url("http://the-internet.herokuapp.com/status_codes/500")
    # use http not https 
    page.pause()




#  PS C:\Users\pc\Documents\playwright> & C:/Users/pc/Documents/playwright/venv/Scripts/Activate.ps1