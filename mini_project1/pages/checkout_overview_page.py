from playwright.sync_api import Page
from mini_project1.locators.checkout_overview_locators import checkout_overview

class checkout_overview_Page:
    def __init__(self, page: Page):
        self.page = page
        self.locator = checkout_overview(page)

    def check(self):
        total_text = self.locator.total.inner_text()
        total_bill = float(total_text.split("$")[1])

        items_price = self.locator.price
        count = items_price.count()

        calculated_total = 0.0
        for i in range(count):
            price_text = items_price.nth(i).inner_text()
            price = float(price_text.replace("$", "").strip())
            calculated_total += price

        assert calculated_total == total_bill, (
            f"Mismatch! Calculated={calculated_total}, Displayed={total_bill}"
        )

    def pay_bill(self):
        self.locator.finish.click()
