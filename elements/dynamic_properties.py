from playwright.sync_api import Page , expect

def test_dynamic_properties(page:Page):
    page.goto("https://demoqa.com/dynamic-properties")
    expect(page.locator("#colorChange")).to_be_visible()
    expect(page.locator("#visibleAfter")).to_be_visible()