from playwright.sync_api import Page , expect

class locators:
    def __init__(self,page:Page):
        self.page=page
        self.home_expand=page.get_by_role("button",name='Toggle')
        self.home=page.get_by_text("Home")
        self.desktop=page.get_by_text("Documents").locator("xpath=../preceding-sibling::*[1]")
        self.check_desk=self.desktop.locator("xpath=ancestor::li[contains(@class,'rct-node')][1]")
        self.notes=page.get_by_text("Office")

    def load(self):
        self.page.goto("https://demoqa.com/checkbox")
        expect(self.page.locator(".text-center")).to_have_text("Check Box")
