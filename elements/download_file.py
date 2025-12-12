from playwright.sync_api import Page , expect

def test_download_file(page:Page):
    page.goto("https://demoqa.com/upload-download")
    with page.expect_download() as download_info:
        page.locator(".btn.btn-primary").get_by_text("Download").click()
    download = download_info.value

    download.save_as("C:/Users/pc/Documents/playwright/elements" + download.suggested_filename)
    
    
    page.pause()