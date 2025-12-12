def test_create_and_login(playwright):

    # Create user using API
    api = playwright.request.new_context()
    new_user = api.post("https://example.com/createUser", data={"name": "Harshit"}).json()

    # Use created user in UI
    page = playwright.chromium.launch().new_page()
    page.goto("https://example.com/login")

    page.fill("#username", new_user["username"])
    page.fill("#password", "123456")
    page.click("#loginButton")
