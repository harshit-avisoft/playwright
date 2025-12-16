from playwright.sync_api import Page, expect
from mini_project1.locators.login_page_locators import LoginLocators
# from mini_project1.pages.dashboard_page import DashboardPage

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.locator = LoginLocators(page)

    def load(self):
        self.page.goto("https://www.saucedemo.com")

    
    def login(self, user,pwd):
        self.locator.username.fill(user)
        self.locator.password.fill(pwd)
        self.locator.login_button.click()
        
        # self.page.pause()

        # return DashboardPage(self.page)
    
    def login_locked_out_user(self,user,pwd):
        self.locator.username.fill(user)
        self.locator.password.fill(pwd)
        self.locator.login_button.click()
        expect(self.locator.error_locked_out_user).to_have_text("Epic sadface: Sorry, this user has been locked out.")

    def check_credentials(self,user,pwd):
        self.locator.username.fill(user)
        self.locator.password.fill(pwd)
        self.locator.login_button.click()
        expect(self.locator.error).to_have_text("Epic sadface: Username and password do not match any user in this service")
