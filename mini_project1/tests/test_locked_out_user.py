from mini_project1.pages.login_page import LoginPage
from mini_project1.pages.dashboard_page import DashboardPage
from mini_project1.pages.cart_page import cartPage
from mini_project1.pages.checkout_page import checkout_Page
from mini_project1.pages.checkout_overview_page import checkout_overview_Page


def test_locked_out_user(page):
    login = LoginPage(page)
    login.load()
    login.login_locked_out_user("locked_out_user", "secret_sauce")
