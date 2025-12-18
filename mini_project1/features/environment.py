import sys
import os
from playwright.sync_api import sync_playwright

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, PROJECT_ROOT)


def before_scenario(context, scenario):
    context.playwright = sync_playwright().start()
    browser = context.playwright.chromium.launch(headless=False)
    context.page = browser.new_page()


def after_scenario(context, scenario):
    context.page.context.browser.close()
    context.playwright.stop()
