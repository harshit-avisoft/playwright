from playwright.sync_api import Page , expect

def test_practice_forms(page:Page):
    page.goto("https://demoqa.com/automation-practice-form")
    
    expect(page).to_have_url("https://demoqa.com/automation-practice-form")
    expect(page.locator("div.practice-form-wrapper > h1.text-center")).to_be_visible()
    
    # first name
    first_name=page.get_by_placeholder("First Name")
    first_name.type("Harshit")
    expect(page.locator("#firstName")).to_have_value("Harshit")
    # expect(page.locator("#firstName")).to_have_text("Harshit")❌
    
    # last name
    last_name=page.get_by_placeholder("Last Name")
    last_name.fill("Pandey")
    expect(page.get_by_placeholder("Last Name")).to_have_value("Pandey")
    
    # email
    email=page.locator("#userEmail")
    email.fill("abc@gmail.com")
    expect(page.locator("#userEmail")).to_have_value("abc@gmail.com")
    
    # gender
    gender=page.get_by_text("Male",exact=True)
    gender.click()
    # mobile
    mobile=page.get_by_placeholder("Mobile Number")
    mobile.fill("1234567890")
    expect(page.get_by_placeholder("Mobile Number")).to_have_value("1234567890")
    
    # dob
    dob=page.locator("#dateOfBirthInput")
    dob.click()
    page.locator(".react-datepicker__month-select").click()
    page.locator(".react-datepicker__month-select").select_option("October")
    page.locator(".react-datepicker__year-select").click()
    page.locator(".react-datepicker__year-select").select_option("2002")
    page.get_by_role("option", name="Choose Tuesday, October 15th,").click()
    expect(page.locator("#dateOfBirthInput")).to_have_value("15 Oct 2002")
    # page.keyboard.press("Escape")
     
    # # subjects
    page.locator("#subjectsContainer > div > div.subjects-auto-complete__value-container.subjects-auto-complete__value-container--is-multi.css-1hwfws3").click()
    page.keyboard.type("English")
    page.keyboard.press("Enter")
    page.keyboard.type("Maths")
    page.keyboard.press("Enter")
    expect(page.locator("#subjectsContainer > div > div.subjects-auto-complete__value-container.subjects-auto-complete__value-container--is-multi.css-1hwfws3")).to_contain_text("English")
    
    # hobbies
    sports=page.get_by_text("Sports")
    sports.click()
    music=page.get_by_text("Music")
    music.click()
    # page.locator("label[for='hobbies-checkbox-1']").click()
    # page.locator("label[for='hobbies-checkbox-2']").click()
    # page.get_by_label("Sports").click()❌
    # page.get_by_label("Music").click()❌
    # page.locator("#hobbies-checkbox-1").click()❌
    # page.locator("#hobbies-checkbox-3").click()❌
    
    # picture
    page.get_by_text("Select picture").set_input_files("C:/Users/pc/Downloads/myfile.png")
    # expect(page.get_by_label("uploadPicture")).to_contain_text("sampleFile.")
    
    # current-address
    address=page.locator("#currentAddress")
    address.fill("Jammu")
    expect(page.locator("#currentAddress")).to_have_value("Jammu")
    
    # state
    state=page.get_by_text("Select State")
    state.click()
    page.keyboard.type("NCR")
    page.keyboard.press("Enter")
    page.keyboard.press("Tab")
    expect(page.locator("#state")).to_have_text("NCR")
    # expect(page.locator("#state")).to_have_value("NCR")❌
    
    # city
    city=page.get_by_text("Select City")
    city.click()
    page.keyboard.type("Delhi")
    page.keyboard.press("Enter")
    page.keyboard.press("Tab")
    expect(page.locator("#city")).to_have_text("Delhi")

    # submit
    submit=page.locator("#submit")
    submit.click()

    page.pause()