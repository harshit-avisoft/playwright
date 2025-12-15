import random
from playwright.sync_api import Page, expect
from mini_project1.locators.dashboard_locators import Dashboard_locators
# from mini_project1.pages.cart_page import cartPage

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.locator = Dashboard_locators(page)
        expect(self.locator.dashboard_logo).to_have_text("Swag Labs")

    def add_to_cart(self, count: int):
        buttons = self.locator.add_to_cart_buttons
        remove_buttons = self.locator.remove_buttons
        total_add_to_cart_buttons=buttons.count()
        assert buttons.count() >= count, "Not enough items to add"

        for _ in range(count):
            buttons.first.click()
        
        assert total_add_to_cart_buttons==(buttons.count() + remove_buttons.count()),"button is not clicked"
    
    def remove_from_cart(self, count: int):
        buttons = self.locator.add_to_cart_buttons
        remove_buttons = self.locator.remove_buttons
        total_add_to_cart_buttons=buttons.count()
        total_remove_buttons=remove_buttons.count()
        assert count<remove_buttons.count(), "Not enough items to remove"

        for _ in range(count):
            remove_buttons.first.click()

        assert remove_buttons.count()+buttons.count()==total_add_to_cart_buttons+total_remove_buttons,"remove button is not clickable"

    def check_cart_count(self):
        remove_buttons=self.locator.remove_buttons
        added_items_count = remove_buttons.count()

        badge_count = int(self.locator.cart_count.inner_text())

        assert added_items_count == badge_count, (f"Cart count mismatch: buttons={added_items_count}, badge={badge_count}")
    
    def logout(self):
        self.locator.navigate.click()
        self.locator.logout.click()
        
    def open_cart(self):
        self.locator.cart.click()
        self.page.pause()
        # return cartPage(self.page)

    def sort_ascending(self):
        page=self.page
        self.locator.sort_by.select_option("Name (A to Z)")

        names=[]
        items=page.locator("div.inventory_item_name")
        count=items.count()

        for i in range(count):
            name_text = items.nth(i).inner_text()
            names.append(name_text)

        assert names == sorted(names), "Product names are NOT sorted A to Z!"
        # page.pause()    

    def sort_low_to_high(self):
        page=self.page
        self.locator.sort_by.select_option("Price (low to high)")
  
        prices = []
        items = page.locator("div.pricebar div")  
        count = items.count()

        for i in range(count):
           price_text = items.nth(i).inner_text().replace("$", "").replace('"', "")
           prices.append(float(price_text))

        assert prices == sorted(prices), "Prices are not sorted low to high!"  
        # page.pause()

    
    def sort_descending(self):
        page = self.page
        self.locator.sort_by.select_option("Name (Z to A)")

        names = []
        items = page.locator("div.inventory_item_name")
        count = items.count()

        for i in range(count):
            name_text = items.nth(i).inner_text()
            names.append(name_text)

        assert names == sorted(names, reverse=True), ("Product names are NOT sorted Z to A!")
        # page.pause()


    def sort_high_to_low(self):
        page = self.page
        self.locator.sort_by.select_option("Price (high to low)")

        prices = []
        items = page.locator("div.pricebar div")
        count = items.count()

        for i in range(count):
            price_text = items.nth(i).inner_text().replace("$", "").strip()
            prices.append(float(price_text))

        assert prices == sorted(prices, reverse=True), ("Prices are NOT sorted high to low!")
        # page.pause()

   
    