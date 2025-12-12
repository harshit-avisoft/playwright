from playwright.sync_api import Page, expect
from mini_project1.locators.dashboard_locators import DashboardPage
from mini_project1.pages.cart_functions import cartFunctions

class DashboardFunctions:
    def __init__(self, page: Page):
        self.page = page
        self.locator = DashboardPage(page)

    def add_to_cart(self):
        self.locator.onesie.click()
        self.locator.backpack.click()

    def check_cart_count(self):
        expect(self.locator.cart_count).to_have_text("2")

    def open_cart(self):
        self.locator.cart.click()
        # self.page.pause()
        return cartFunctions(self.page)
    
    def backpack_detail(self):
        self.locator.backpack_detail.click()

    def ascending(self):
        page=self.page
        self.locator.sort_by.select_option("az")

        names=[]
        items=page.locator("div.inventory_item_name")
        count=items.count()

        for i in range(count):
            name_text = items.nth(i).inner_text()
            names.append(name_text)

        assert names == sorted(names), "Product names are NOT sorted A to Z!"
        page.pause()

    def descending(self):
        page=self.page
        self.locator.sort_by.select_option("za")

        names=[]
        items=page.locator("div.invetory_item_name")
        count=items.count()

    def low_to_high(self):
        page=self.page
        self.locator.sort_by.select_option("Price (low to high)")
  
        # page.wait_for_timeout(500)
        prices = []
        items = page.locator("div.pricebar div")  
        count = items.count()

        for i in range(count):
           price_text = items.nth(i).inner_text().replace("$", "").replace('"', "")
           prices.append(float(price_text))

        assert prices == sorted(prices), "Prices are not sorted low to high!"  
        # page.pause()


    def high_to_low(self):
        pass
    