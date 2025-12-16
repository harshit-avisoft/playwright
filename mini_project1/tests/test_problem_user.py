from mini_project1.pages.login_page import LoginPage
from mini_project1.pages.dashboard_page import DashboardPage
from mini_project1.pages.cart_page import cartPage
from mini_project1.pages.checkout_page import checkout_Page
from mini_project1.pages.checkout_overview_page import checkout_overview_Page



def test_problem_user(page):
    login=LoginPage(page)
    login.load()
    login.login("problem_user","secret_sauce")
    assert "inventory" in page.url

    dashboard = DashboardPage(page)
    # dashboard.add_to_cart(3)
    dashboard.remove_from_cart(2)
    dashboard.sort_low_to_high()
    dashboard.sort_ascending()