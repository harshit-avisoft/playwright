from playwright.sync_api import Page

class checkout:
    def __init__(self,page=Page):
        self.page=page
        self.first_name=page.locator("#first-name")
        self.last_name=page.locator("#last-name")
        self.postal_code=page.locator("#postal-code")
        self.cancel=page.locator("#cancel")
        self.continuee=page.locator("#continue")
        self.error = page.locator("h3[data-test='error']")
        self.cart_page_title = page.locator("span[data-test='title']")