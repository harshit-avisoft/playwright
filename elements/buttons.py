from playwright.sync_api import Page, expect

def test_buttons(page:Page):
    page.goto("https://demoqa.com/buttons")
    # page.locator("#doubleClickBtn").dblclick()
    # page.locator("#rightClickBtn").click(button="right")
    page.locator("button.btn.btn-primary").nth(2).click()