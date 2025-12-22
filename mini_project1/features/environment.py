import sys
import os
from playwright.sync_api import sync_playwright
import allure

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, PROJECT_ROOT)


def before_scenario(context, scenario):
    context.playwright = sync_playwright().start()
    # browser = context.playwright.firefox.launch(headless=False)
    browser = context.playwright.chromium.launch(headless=True)
    context.page = browser.new_page()


def after_scenario(context, scenario):
    if scenario.status == "failed":
        allure.attach(
            context.page.screenshot(),
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        
    context.page.context.browser.close()
    context.playwright.stop()

# Hooks are special functions that run automatically at certain points
# They are defined in environment.py
# behave calls them autoatically

# hooks execution order
# before_all
#   before_feature
#     before_scenario
#       before_step
#         STEP
#       after_step
#     after_scenario
#   after_feature
# after_all


# from playwright.sync_api import sync_playwright

# def before_scenario(context, scenario):
#     print(f"Starting scenario: {scenario.name}")
    
#     context.playwright = sync_playwright().start()
#     context.browser = context.playwright.chromium.launch(headless=False)
#     context.context = context.browser.new_context()
#     context.page = context.context.new_page()

# def after_scenario(context, scenario):
#     print(f"Finished scenario: {scenario.name}")
    
#     context.browser.close()
#     context.playwright.stop()


# Using Hooks for Login
# def before_scenario(context, scenario):
#     context.page.goto("https://www.saucedemo.com")
#     context.page.fill("#user-name", "standard_user")
#     context.page.fill("#password", "secret_sauce")
#     context.page.click("#login-button")

# conditional hooks
# @ui
# Scenario: Login test

# def before_scenario(context, scenario):
#     if "ui" in scenario.tags:
#         print("UI scenario detected")

# after scenario with screenshot on failure

# import os

# def after_scenario(context, scenario):
#     if scenario.status == "failed":
#         os.makedirs("screenshots", exist_ok=True)
#         context.page.screenshot(
#             path=f"screenshots/{scenario.name}.png"
#         )

# before_feature and after_feature example

# def before_feature(context, feature):
#     print(f"Starting feature: {feature.name}")

# def after_feature(context, feature):
#     print(f"Finished feature: {feature.name}")


# before_all and after_all
# def before_all(context):
#     print("Setting up test environment")

# def after_all(context):
#     print("Cleaning up test environment")


# before_step & after_step (Rare but Useful)
# def before_step(context, step):
#     print(f"Running step: {step.name}")

# def after_step(context, step):
#     if step.status == "failed":
#         print("Step failed")