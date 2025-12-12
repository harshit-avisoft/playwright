from playwright.sync_api import Page,expect

def test_browser_windows(page:Page,context):
    page.goto("https://demoqa.com/browser-windows")
    expect(page).to_have_url("https://demoqa.com/browser-windows")
    
    # new tab
    new_tab=page.locator("#tabButtonWrapper button")
    with context.expect_page() as new_page_info:
        new_tab.click()
    new_tab = new_page_info.value
    expect(new_tab).to_have_url("https://demoqa.com/sample")

    new_tab.close()

    page.bring_to_front()
    
    # new window
    new_window=page.locator("#windowButton")
    with context.expect_page() as new_window_info:
        new_window.click()
    new_window=new_window_info.value
    expect(new_window).to_have_url("https://demoqa.com/sample")
    
    new_window.close()
    page.bring_to_front()
        

    # new window message
    new_window_message=page.locator("#messageWindowButton")
    with context.expect_page() as new_window_message_info:
        new_window_message.click()
    new_window_message=new_window_message_info.value
    # expect(new_window_message).to_have_url("about:blank") not working
    
    new_window_message.close()
    page.bring_to_front()

    page.pause()