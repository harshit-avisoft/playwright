from behave import given, when, then
from playwright.sync_api import sync_playwright

@given("Given user is on the login page")
def step_open_login(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.page.goto("https://www.saucedemo.com")

@when("When user enters valid username and password")
def step_enter_credentials(context):
    context.page.fill("#user-name", "standard_user")
    context.page.fill("#password", "secret_sauce")

@when("click on the login button")
def step_click_login(context):
    context.page.click("#login-button")

@then("I should see the dashboard")
def step_verify_dashboard(context):
    assert context.page.url.endswith("inventory.html")
    context.browser.close()
    context.playwright.stop()
