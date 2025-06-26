import time

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_info(self, first, last, zip_code):
        time.sleep(1)
        self.driver.find_element("id", "first-name").send_keys(first)
        time.sleep(1)
        self.driver.find_element("id", "last-name").send_keys(last)
        time.sleep(1)
        self.driver.find_element("id", "postal-code").send_keys(zip_code)
        time.sleep(1)
        self.driver.find_element("id", "continue").click()
        time.sleep(1)

    def finish_checkout(self):
        time.sleep(1)
        self.driver.find_element("id", "finish").click()
        time.sleep(2)

    def get_complete_text(self):
        time.sleep(1)
        return self.driver.find_element("class name", "complete-header").text
