from mini_project1.pages.login_page import LoginPage
from mini_project1.pages.dashboard_page import DashboardPage
from mini_project1.pages.cart_page import cartPage
from mini_project1.pages.checkout_page import checkout_Page
from mini_project1.pages.checkout_overview_page import checkout_overview_Page



def test_valid_purchase(page):

    login=LoginPage(page)
    login.load()
    login.login("standard_user","secret_sauce")  
    assert "inventory" in page.url

    
    dashboard = DashboardPage(page)
    dashboard.add_to_cart(5)
    dashboard.remove_from_cart(1)
    dashboard.check_cart_count()
    dashboard.sort_high_to_low()
    dashboard.open_cart()
    
    cart=cartPage(page)
    cart.verify_cart_items_count()
    cart.checkout()

    checkout=checkout_Page(page)
    checkout.fill_detail("Harshit","Pandey","abc")
    # checkout.cancel()

    checkout_overview=checkout_overview_Page(page)
    checkout_overview.check_total()
    checkout_overview.pay_bill()