from playwright.sync_api import Page, expect

class LinksPage:
    def __init__(self, page: Page):
        self.page = page
        self.created_link = page.locator("#created")
        self.link_response = page.locator("p#linkResponse")
        self.simple_link = page.locator("#simpleLink")

    def open(self):
        self.page.goto("https://demoqa.com/links")

    def click_created(self):
        self.created_link.click()

    def verify_created_message(self):
        expect(self.link_response).to_contain_text("Created")

    def click_simple_link_and_wait_for_new_tab(self, context):
        with context.expect_page() as new_page_info:
            self.simple_link.click()
        return new_page_info.value
