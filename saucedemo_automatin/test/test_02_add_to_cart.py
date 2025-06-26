def test_add_to_cart(driver, login_page, inventory_page):
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_first_item_to_cart()
    assert inventory_page.get_cart_badge_count() == "1"