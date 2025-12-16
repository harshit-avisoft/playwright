from playwright.sync_api import Page,expect
from mini_project1.locators.checkout_locators import checkout

class checkout_Page:
    def __init__(self, page: Page):
        self.page = page
        self.locator = checkout(page)
        expect(self.locator.cart_page_title).to_have_text("Checkout: Your Information")

    def fill_detail(self, firstname=None, lastname=None, postalcode=None):
     if firstname:
        self.locator.first_name.fill(firstname)
     if lastname:
        self.locator.last_name.fill(lastname)
     if postalcode:
        self.locator.postal_code.fill(postalcode)

     self.locator.continuee.click()

     if not firstname:
        expect(self.locator.error).to_have_text("Error: First Name is required")
     elif not lastname:
        expect(self.locator.error).to_have_text("Error: Last Name is required")
     elif not postalcode:
        expect(self.locator.error).to_have_text("Error: Postal Code is required")
       
        # self.page.pause()


    def cancel(self):
        self.locator.cancel.click()
    
    def checkout_firstname(self, firstname=None, lastname=None, postalcode=None):
        self.locator.continuee.click()
        expect(self.locator.error,"Error: First Name is required").not_to_have_text("Error: First Name is required")
        # assert self.locator.error.to_have_text("") , "no first name"
