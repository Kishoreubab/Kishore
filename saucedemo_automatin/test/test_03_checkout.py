def test_checkout(driver, login_page, inventory_page, cart_page, checkout_page):
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()
    cart_page.click_checkout()
    checkout_page.fill_checkout_info("Holder", "Fin", "65656")
    checkout_page.finish_checkout()
    assert "Thank you" in checkout_page.get_complete_text()