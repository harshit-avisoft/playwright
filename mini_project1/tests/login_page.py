from mini_project1.pages.login_page_functions import LoginPage

def test_login(page):
    login = LoginPage(page)
    
    login.load()
    dashboard=login.login("standard_user", "secret_sauce")
    # login.error()

    # Assertion
    assert "inventory" in page.url
    

    dashboard.add_to_cart()
    dashboard.check_cart_count()
    # dashboard.low_to_high()
    dashboard.ascending()
    dashboard.open_cart()