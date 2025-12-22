from behave import given, when, then
from playwright.sync_api import expect
from pages.cart_page import cartPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.crypto_utils import user_name, password
from helpers.session import ensure_user_logged_in
 

def ensure_cart_page(context):
    ensure_user_logged_in(context)
    if not hasattr(context, "cart_page"):
        context.page.locator(".shopping_cart_link").click()
        context.cart_page = cartPage(context.page)
 

@given("user navigates to cart page")
def step_open_cart(context):
    ensure_cart_page(context)


@then("cart items count should match badge count")
def step_verify_cart_items(context):
    ensure_cart_page(context)

    # Count cart items on cart page
    items_count = context.page.locator("div.cart_item").count()

    # Check if badge exists
    badge_locator = context.page.locator(".shopping_cart_badge")

    if badge_locator.count() == 0:
        # No badge means cart should be empty
        assert items_count == 0, (
            f"Expected empty cart, but found {items_count} items"
        )
    else:
        badge_count = int(badge_locator.inner_text())
        assert items_count == badge_count, (
            f"Cart items mismatch: page={items_count}, badge={badge_count}"
        )


@when("user proceeds to checkout")
def step_checkout(context):
    ensure_cart_page(context)
    context.cart_page.checkout()


@then("checkout page should be displayed")
def step_verify_checkout(context):
    # Wait until the page URL contains 'checkout'
    context.page.wait_for_url("**checkout*")


@given("user has {count:d} products in the cart")
@given("user has {count:d} product in the cart")
@when("user has {count:d} products in the cart")
@when("user has {count:d} product in the cart")
def step_user_has_these_products(context, count):
    ensure_cart_page(context)
    current_count = context.cart_page.locator.remove.count()
    to_add = count - current_count
    # assert to_add==0 , ("abc")
    