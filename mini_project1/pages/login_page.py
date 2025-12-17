from playwright.sync_api import Page, expect
from mini_project1.locators.login_page_locators import LoginLocators
# from mini_project1.pages.dashboard_page import DashboardPage
from cryptography.fernet import Fernet
from mini_project1.utils.crypto_utils import key,user_name,password

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.locator = LoginLocators(page)

    def load(self):
        self.page.goto("https://www.saucedemo.com")

    
    def login(self, user,pwd):
        fernet=Fernet(key)
        dec_user = fernet.decrypt(user).decode()
        dec_pwd = fernet.decrypt(pwd).decode()

        self.locator.username.fill(dec_user)
        self.locator.password.fill(dec_pwd)
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
