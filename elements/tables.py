from playwright.sync_api import Page , expect

def test_tables(page:Page):
    page.goto("https://demoqa.com/webtables")
    # search
    page.locator("#searchBox").fill("Cierra")
    page.locator("#searchBox").fill("")
    # add new record
    page.locator("#addNewRecordButton").click()
    page.locator("#firstName").fill("Raj")
    page.locator("#lastName").fill("kumar")
    page.locator("#userEmail").fill("raj@123.com")
    page.locator("#age").fill("18")
    page.locator("#salary").fill("120000")
    page.locator("#department").fill("spy")
    page.locator("#submit").click()
    expect(page.locator("div.rt-tbody")).to_contain_text("Raj")
    # expect(page.get_by_text("Raj")).to_be_visible()

    # delete
    page.locator("#delete-record-1 > svg").click()

    # edit
    page.locator("#edit-record-2 > svg").click()
    page.locator("#age").fill("33")
    page.locator("#submit").click()

    
    page.locator("span.select-wrap.\\-pageSizeOptions").click()
    page.locator("span.select-wrap.-pageSizeOptions select").select_option("5")
    # page.locator("span.select-wrap.-pageSizeOptions > select > option[value='5']").click()
    # Because browsers don’t accept click() on <option>
    # Options are not exposed as real clickable UI elements.
    page.pause()
    