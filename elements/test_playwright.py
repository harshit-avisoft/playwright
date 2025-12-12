import re
# from tkinter.filedialog import test
from playwright.sync_api import Page, expect

# def test_has_title(page: Page):
#     page.goto("https://demoqa.com/text-box")

    # expect(page).to_have_title(re.compile("Playwright"))

def test_enter_name(page: Page):
    page.goto("https://demoqa.com/text-box")
    
    page.locator("#userName").fill("Harshit")
    page.locator("#userEmail").fill("hp@abc.com")
    page.locator("#currentAddress").fill("Jammu")
    page.locator("#permanentAddress").fill("Vaishali")
    
    page.locator("#submit").click()
    
    page.pause()

# def test_get_started_link(page: Page):
#     page.goto("https://demoqa.com/text-box")

#     page.get_by_role("link", name="Get started").click()

#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()