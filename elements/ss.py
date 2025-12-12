import re
from playwright.sync_api import Page , expect

def test_ss(page:Page):
    page.goto("https://google.com")
    search_box=page.locator("textarea").nth(0)
    search_box.fill("Playwright Python")
    page.get_by_role("button", name="Google Search").click()
    page.pause()
    page.screenshot(path="search_result.png")