from playwright.sync_api import Page, expect

def test_alerts(page: Page):
    page.goto("https://demoqa.com/alerts")
    expect(page.locator(".text-center")).to_have_text("Alerts")

    # first 
    first_button = page.locator("#alertButton")
    with page.expect_event("dialog") as dlg1:
        first_button.click()
    alert = dlg1.value
    assert alert.message == "You clicked a button"
    alert.accept()

    # confirm dialog 
    third_button = page.locator("#confirmButton")
    with page.expect_event("dialog") as dlg2:
        third_button.click()
    alert = dlg2.value
    assert alert.message == "Do you confirm action?"
    alert.accept()
    expect(page.locator("#confirmResult")).to_have_text("You selected Ok")

    # prompt dialog — 
    fourth_button = page.locator("#promtButton")
    with page.expect_event("dialog") as dlg3:
        fourth_button.click()
    alert = dlg3.value
    alert.accept("Harshit")
    expect(page.locator("#promptResult")).to_have_text("You entered Harshit")