from pages.cart_page import cartPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.crypto_utils import user_name, password

def ensure_user_logged_in(context):
    if not hasattr(context, "dashboard_page"):
        login_page = LoginPage(context.page)
        login_page.load()
        login_page.login(user_name, password)
        context.dashboard_page = DashboardPage(context.page)