from behave import given, when, then
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.crypto_utils import user_name, password
from helpers.session import ensure_user_logged_in


@given("user is logged in")
def step_user_logged_in(context):
    ensure_user_logged_in(context)


@given("user has {count:d} products in the dashboard cart")
@given("user has {count:d} product in the dashboard cart")
@when("user has {count:d} products in the dashboard cart")
@when("user has {count:d} product in the dashboard cart")
def step_user_has_products(context, count):
    ensure_user_logged_in(context)
    current_count = context.dashboard_page.locator.remove_buttons.count()
    to_add = count - current_count
    if to_add > 0:
        context.dashboard_page.add_to_cart(to_add)
    
    context.dashboard_page.check_cart_count()



@when("user adds {count:d} products to the dashboard cart")
@when("user adds {count:d} product to the dashboard cart")
def step_add_products(context, count):
    ensure_user_logged_in(context)
    context.dashboard_page.add_to_cart(count)


@when("user removes {count:d} product from the cart")
def step_remove_products(context, count):
    ensure_user_logged_in(context)
    context.dashboard_page.remove_from_cart(count)


@then("cart badge should be updated correctly")
def step_verify_cart_badge(context):
    ensure_user_logged_in(context)
    context.dashboard_page.check_cart_count()

@when("add '{item_name}' to inventory")
@then("add '{item_name}' to inventory")
def step_add_item_by_name(context,item_name):
    ensure_user_logged_in(context)
    context.dashboard_page.add_by_item_name(item_name)

@when("user remove '{item_name}' from the inventory")
def step_remove_item_by_name(context,item_name):
    ensure_user_logged_in(context)
    context.dashboard_page.remove_by_item_name(item_name)

@when('user sorts items "{order}"')
def step_sort_items(context, order):
    ensure_user_logged_in(context)
    context.dashboard_page.sort_alphabetically(order)


@then('items should be sorted "{order}"')
def step_verify_sorted_items(context, order):
    # validation already happens inside sort_alphabetically
    pass

# @when('user adds {n} products to the dashboard cart')
# def step_page(context, n):
#     ensure_user_logged_in(context)
#     context.dashboard_page.add_to_cart(n)
    