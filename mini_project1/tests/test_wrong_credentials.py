from mini_project1.pages.login_page import LoginPage
from mini_project1.pages.dashboard_page import DashboardPage
from mini_project1.pages.cart_page import cartPage
from mini_project1.pages.checkout_page import checkout_Page
from mini_project1.pages.checkout_overview_page import checkout_overview_Page


def test_wrong_credentials(page):
    login=LoginPage(page)
    login.load()
    login.check_credentials("standard_user1", "secret_sauce")
