from playwright.sync_api import Page, expect
from mini_project1.locators.login_page_locators import LoginLocators
from mini_project1.pages.dashboard_functions import DashboardFunctions

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.locator = LoginLocators(page)

    def load(self):
        self.page.goto("https://www.saucedemo.com")

    def error(self):
        expect(self.locator.error).to_have_text("Epic sadface: Username and password do not match any user in this service")
    
    def login(self, user, pwd):
        self.locator.username.fill(user)
        self.locator.password.fill(pwd)
        self.locator.login_button.click()
        # self.page.pause()
        return DashboardFunctions(self.page)
