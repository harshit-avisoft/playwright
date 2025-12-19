from mini_project1.pages.login_page import LoginPage
from mini_project1.pages.dashboard_page import DashboardPage
from mini_project1.pages.cart_page import cartPage
from mini_project1.pages.checkout_page import checkout_Page
from mini_project1.pages.checkout_overview_page import checkout_overview_Page
from cryptography.fernet import Fernet
from mini_project1.utils.crypto_utils import key
from mini_project1.utils.items import InventoryItems

def test_valid_purchase(page):
    user_name="standard_user"
    password="secret_sauce"
    fernet=Fernet(key)
    encrypted_user_name=fernet.encrypt(user_name.encode())
    encrypted_password=fernet.encrypt(password.encode())

    login=LoginPage(page)
    login.load()
    login.login(encrypted_user_name,encrypted_password)  
    assert "inventory" in page.url

    
    dashboard = DashboardPage(page)
    dashboard.add_to_cart(5)
    dashboard.remove_by_item_name("Sauce Labs Back")
    # dashboard.add_by_item_name("Sauce")
    # dashboard.remove_by_item_name(InventoryItems.BIKE_LIGHT)
    dashboard.remove_from_cart(1)
    dashboard.check_cart_count() 
    # -- not works when count is 0
    dashboard.sort_alphabetically("descendin")
    dashboard.open_cart()
    
    cart=cartPage(page)
    cart.verify_cart_items_count()
    cart.checkout()

    checkout=checkout_Page(page)
    checkout.fill_detail("Harshit","Pandey","abc")

    checkout_overview=checkout_overview_Page(page)
    checkout_overview.check_total()
    checkout_overview.pay_bill()
