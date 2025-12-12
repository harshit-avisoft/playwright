from playwright.sync_api import Page

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.backpack=page.locator("#add-to-cart-sauce-labs-backpack")
        self.bikelight=page.locator("#add-to-cart-sauce-labs-bike-light")
        self.bolttshirt=page.locator("#add-to-cart-sauce-labs-bolt-t-shirt")
        self.fleece=page.locator("#add-to-cart-sauce-labs-fleece-jacket")
        self.onesie=page.locator("#add-to-cart-sauce-labs-onesie")
        self.redtshirt=page.locator("#add-to-cart-test.allthethings()-t-shirt-(red)")
        

        self.all_items=page.locator(".inventory_list")
        self.backpack_detail=page.locator("#item_4_title_link")
        self.sort_by=page.locator("select.product_sort_container")
        self.cart=page.locator(".shopping_cart_link")
        self.cart_count=page.locator(".shopping_cart_badge")
        self.title = page.locator(".title")


    def verify_dashboard_title(self):
        return self.title.inner_text()