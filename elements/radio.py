import re
from playwright.sync_api import Page, expect

def test_radio_buttons(page: Page):
    page.goto("https://demoqa.com/radio-button")
    page.get_by_text("Impressive").click()
    expect(page.get_by_text("You have selected Impressive")).to_be_visible()
    page.pause()