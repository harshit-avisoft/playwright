from playwright.sync_api import Page, expect
from mini_project1.locators.cart_locators import cart

class cartPage:
    def __init__(self, page: Page):
        self.page = page
        self.locator = cart(page)
        expect(self.locator.cart_page_title).to_have_text("Your Cart")

    # def remove(self):
    #     self.locator.remove_backpack.click()
    #     expect(self.locator.cart_count).to_have_text("2")

    def verify_cart_items_count(self):
        cart_items = self.page.locator("div.cart_item")

        items_count = cart_items.count()

        badge_count = int(self.locator.cart_count.inner_text())

        # Assertion
        assert items_count == badge_count, ( f"Cart items mismatch: page={items_count}, badge={badge_count}")

    def checkout(self):
        self.locator.checkout.click()
        # self.page.pause()

    def check_checkout_button_alignment(self):
       classes=self.locator.checkout.get_attribute("class")

       assert "btn_visual_failure" not in classes, (" checkout button is not aligned")
