from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.cart_page import CartPage
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)


def before_scenario(context,scenario):
    context.playwright=sync_playwright().start()
    browser=context.playwright.chromium.launch(headless=False)
    context.page=browser.new_page()

    context.login_page=LoginPage(context.page)
    context.dashboard_page=DashboardPage(context.page)
    context.cart_page=CartPage(context.page)

def after_scenario(context,scenario):
    context.page.context.browser.close()
    context.playwright.stop()