from playwright.sync_api import Page, expect
from mini_project1.locators.cart_locators import cart

class cartFunctions:
    def __init__(self,page:Page):
        self.page=page
        self.locator=cart(page)

    def remove(self):
        self.locator.remove.click()