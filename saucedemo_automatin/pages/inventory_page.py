import time

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_first_item_to_cart(self):
        time.sleep(1)
        self.driver.find_element("xpath", "//button[contains(text(),'Add to cart')]").click()
        time.sleep(1)

    def get_cart_badge_count(self):
        time.sleep(1)
        return self.driver.find_element("class name", "shopping_cart_badge").text

    def go_to_cart(self):
        time.sleep(1)
        self.driver.find_element("class name", "shopping_cart_link").click()
        time.sleep(1)
