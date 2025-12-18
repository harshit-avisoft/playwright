from behave import given, when, then
from playwright.sync_api import expect
from pages.login_page import LoginPage
from utils.crypto_utils import user_name, password


@given("user is on the login page")
def step_open_login_page(context):
    context.login_page = LoginPage(context.page)
    context.login_page.load()


@when("user logs in with valid credentials")
def step_login_valid_user(context):
    context.login_page.login(user_name, password)


@then("user should be logged in successfully")
def step_verify_successful_login(context):
    # Check if URL contains inventory.html (works with different domains)
    context.page.wait_for_url("**inventory.html")
