import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        time.sleep(1)
        self.driver.find_element("id", "checkout").click()
        time.sleep(1)
