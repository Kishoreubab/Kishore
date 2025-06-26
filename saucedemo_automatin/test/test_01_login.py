def test_login(driver, login_page):
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url