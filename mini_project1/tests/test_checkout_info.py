from mini_project1.pages.login_page import LoginPage
from mini_project1.pages.dashboard_page import DashboardPage
from mini_project1.pages.cart_page import cartPage
from mini_project1.pages.checkout_page import checkout_Page
from mini_project1.pages.checkout_overview_page import checkout_overview_Page
from cryptography.fernet import Fernet
from mini_project1.utils.crypto_utils import key

def test_page(page):
    user_name="standard_user"
    password="secret_sauce"
    fernet=Fernet(key)
    encrypted_user_name=fernet.encrypt(user_name.encode())
    encrypted_password=fernet.encrypt(password.encode())
    login = LoginPage(page)
    login.load()
    login.login(encrypted_user_name, encrypted_password)
    assert "inventory" in page.url

    # login.login("standard_user", "secret_sauce1")
    
    dashboard = DashboardPage(page)
    dashboard.add_to_cart(3)
    dashboard.check_cart_count()
    dashboard.sort_high_to_low()
    dashboard.open_cart()
    
    cart=cartPage(page)
    # cart.remove()
    cart.verify_cart_items_count()
    cart.checkout()

    checkout=checkout_Page(page)
    checkout.checkout_firstname(None,"Pandey","abc")
    # checkout.cancel()