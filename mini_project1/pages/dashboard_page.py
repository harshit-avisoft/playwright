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
     add_buttons = self.locator.add_to_cart_buttons
     remove_buttons = self.locator.remove_buttons

     initial_add = add_buttons.count()
     initial_remove = remove_buttons.count()

     assert initial_add >= count, "Not enough items to add"

     for _ in range(count):
         add_buttons.first.click()

     final_add = add_buttons.count()
     final_remove = remove_buttons.count()

     assert final_remove - initial_remove == count, (
         f"Expected {count} items to be added, but only "
         f"{final_remove - initial_remove} were added"
     )
    
    def remove_from_cart(self, count: int):
     add_buttons = self.locator.add_to_cart_buttons
     remove_buttons = self.locator.remove_buttons

     initial_add = add_buttons.count()
     initial_remove = remove_buttons.count()

     assert initial_remove >= count, (f"Not enough items to remove. ")

     for _ in range(count):
         remove_buttons.first.click()

     final_add = add_buttons.count()
     final_remove = remove_buttons.count()

     assert initial_remove - final_remove == count, ("only" f"{initial_remove - final_remove} were removed")

     assert initial_add + initial_remove == final_add + final_remove, (
         "UI state inconsistent after remove operation"
     )
    
    def check_cart_alignment(self):
     cart_container = self.locator.cart_container
     classes = cart_container.get_attribute("class")

     assert "visual_failure" not in classes, (" Cart is not aligned")

    def check_button_alignment(self):
        add_buttons = self.locator.add_to_cart_buttons
        buttons_count=add_buttons.count()
        for i in range(buttons_count):
           classes = add_buttons.nth(i).get_attribute("class")
           assert "btn_inventory_misaligned" not in classes, (" Buttons are not aligned")

    def check_menu_button_alignment(self):
       classes=self.locator.menu_button.get_attribute("class")

       assert "visual_failure" not in classes, (" menu button is not aligned")

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

   
    