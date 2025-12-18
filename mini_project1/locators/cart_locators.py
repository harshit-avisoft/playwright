from playwright.sync_api import Page

class cart:
    def __init__(self,page=Page):
        self.page=page
        self.continue_shopping=page.locator("#continue-shopping")
        self.checkout=page.locator("#checkout")
        self.remove=page.locator(".btn.btn_secondary.btn_small.cart_button")
        self.cart_count=page.locator(".shopping_cart_badge")
        self.cart_page_title = page.locator("span[data-test='title']")