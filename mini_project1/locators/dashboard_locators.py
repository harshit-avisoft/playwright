from playwright.sync_api import Page

class Dashboard_locators:
    def __init__(self, page: Page):
        self.page = page
        # self.backpack=page.locator("#add-to-cart-sauce-labs-backpack")
        # self.bikelight=page.locator("#add-to-cart-sauce-labs-bike-light")
        # self.bolttshirt=page.locator("#add-to-cart-sauce-labs-bolt-t-shirt")
        # self.fleece=page.locator("#add-to-cart-sauce-labs-fleece-jacket")
        # self.onesie=page.locator("#add-to-cart-sauce-labs-onesie")
        # self.redtshirt=page.locator("#add-to-cart-test.allthethings()-t-shirt-(red)")
        
        self.add_to_cart_buttons = page.locator("button.btn.btn_primary.btn_small.btn_inventory")
        self.remove_buttons = page.locator("button.btn.btn_secondary.btn_small.btn_inventory")
        
        self.navigate=page.locator("#react-burger-menu-btn")
        self.menu_button=page.locator(".bm-burger-button img.bm-icon")
        self.logout=page.locator("#logout_sidebar_link")
        
        self.all_items=page.locator(".inventory_list")
        
        self.sort_by=page.locator("select.product_sort_container")
        
        self.cart_container=page.locator("#shopping_cart_container")
        self.cart=page.locator(".shopping_cart_link")
        self.cart_count=page.locator(".shopping_cart_badge")
       
        self.title = page.locator(".title")
        self.dashboard_logo=page.locator(".app_logo")


    def verify_dashboard_title(self):
        return self.title.inner_text()
    