from playwright.sync_api import Page

class cart:
    def __init__(self,page=Page):
        self.page=page
        self.continue_shopping=page.locator("#continue-shopping")
        self.checkout=page.locator("#checkout")
        self.remove=page.locator("#remove-sauce-labs-backpack")
        
    