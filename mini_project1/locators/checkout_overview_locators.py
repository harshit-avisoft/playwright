from playwright.sync_api import Page

class checkout_overview:
    def __init__(self,page=Page):
        self.page=page
        self.price=page.locator(".inventory_item_price")
        self.total=page.locator(".summary_subtotal_label")
        self.cancel=page.locator("#cancel")
        self.finish=page.locator("#finish") 