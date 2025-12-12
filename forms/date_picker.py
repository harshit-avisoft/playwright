from playwright.sync_api import Page,expect

def test_date_picker(page:Page):
    page.goto("https://demoqa.com/date-picker")
    dob=page.locator("#dateOfBirthInput")
    dob.click()
    page.locator(".react-datepicker__month-select").click()
    page.locator(".react-datepicker__month-select").select_option("October")
    page.locator(".react-datepicker__year-select").click()
    page.locator(".react-datepicker__year-select").select_option("2002")
    page.get_by_role("option", name="Choose Tuesday, October 15th,").click()
    expect(page.locator("#dateOfBirthInput")).to_have_value("15 Oct 2002")