from pages.links import LinksPage
from playwright.sync_api import Page , expect

def test_links(page: Page, context):
    links = LinksPage(page)

    links.open()

    links.click_created()
    links.verify_created_message()

    new_page = links.click_simple_link_and_wait_for_new_tab(context)
    expect(new_page).to_have_url("https://demoqa.com/")

    new_page.close()
    page.bring_to_front()
    page.pause()
