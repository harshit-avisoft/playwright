from behave import given,when,then
from playwright.sync_api import sync_playwright

@given("User logged in")
def step_logged_in(context):
    context.login_page.open()
    context.login_page.login("standard_user","secret_sauce")

@when("Add a product to cart")
def step_add_to_cart(context):
    context.dashboard_page.add_random_product()

@then("the product should appear in the cart")
def step_verify_cart(context):
    context.cart_page.verify_product_added()