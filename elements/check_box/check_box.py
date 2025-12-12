from playwright.sync_api import Page, expect
import pytest
from elements.check_box.locators import locators


def test_radio_buttons(page: Page):
    Locators=locators(page)

    Locators.load()

    expect(page.locator(".text-center")).to_have_text("Check Box")

    Locators.home_expand.click()
    
    check_home=Locators.home.locator("xpath=ancestor::li[contains(@class,'rct-node')][1]")
    expect(check_home).to_have_class("rct-node rct-node-parent rct-node-expanded")

    Locators.desktop.click()

    expect(Locators.check_desk).to_have_class("rct-node rct-node-parent rct-node-expanded")
    
    Locators.notes.click()
    page.pause()


    # page.locator("svg.rct-icon.rct-icon-expand-close").nth(0).click()
    # page.locator("svg.rct-icon.rct-icon-uncheck").nth(2).click()