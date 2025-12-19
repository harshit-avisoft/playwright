from behave import given, when, then
from playwright.sync_api import expect
from pages.login_page import LoginPage
from utils.crypto_utils import  password


@given("user is on the login page")
@then("user is on the login page")
def step_open_login_page(context):
    context.login_page = LoginPage(context.page)
    context.login_page.load()


@when("'{user_name}' logs in with valid credentials")
def step_login_valid_user(context,user_name):
    context.login_page.login(user_name, password)


@then("user should be logged in successfully")
def step_verify_successful_login(context):
    # Check if URL contains inventory.html (works with different domains)
    context.page.wait_for_url("**inventory.html")

@when("'{user_name}' logs in")
def step_locked_user_login(context,user_name):
    context.login_page.login_locked_out_user(user_name,password)

@when("'{user_name}' logs in with wrong password '{pwd}'")
def step_wrong_password(context,user_name,pwd):
    context.login_page.login(user_name,pwd)

@then("error message should be displayed '{user_name}' '{pwd}'")
def step_error_message(context,user_name,pwd):
    context.login_page.check_credentials(user_name,pwd)
    