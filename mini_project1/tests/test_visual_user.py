from mini_project1.pages.login_page import LoginPage
from mini_project1.pages.dashboard_page import DashboardPage
from mini_project1.pages.cart_page import cartPage
from mini_project1.pages.checkout_page import checkout_Page
from mini_project1.pages.checkout_overview_page import checkout_overview_Page
from cryptography.fernet import Fernet
from mini_project1.utils.crypto_utils import key,user_name,password

def test_visual_user(page):
    # key=Fernet.generate_key()
    fernet=Fernet(key)
    encrypted_user_name=fernet.encrypt(user_name.encode())
    encrypted_password=fernet.encrypt(password.encode())

    login=LoginPage(page)
    login.load()
    login.login(encrypted_user_name,encrypted_password)
    assert "inventory" in page.url

    dashboard = DashboardPage(page)
    dashboard.add_to_cart(3)
    # dashboard.check_menu_button_alignment()
    # dashboard.check_button_alignment()
    # dashboard.check_cart_alignment()
    # dashboard.sort_low_to_high()
    dashboard.open_cart()
    
    cart=cartPage(page)
    cart.verify_cart_items_count()
    cart.check_checkout_button_alignment()
