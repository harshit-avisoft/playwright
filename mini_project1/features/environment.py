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
