from playwright.sync_api import Page , expect

def test_upload_file(page: Page):
    page.goto("https://demoqa.com/upload-download")
    page.get_by_text("Select a file").set_input_files("C:/Users/pc/Downloads/myfile.png")
    expect(page.locator("#uploadedFilePath")).to_contain_text("myfile.png")
    page.pause()
    # page.screenshot(path="ss.png", full_page=True)