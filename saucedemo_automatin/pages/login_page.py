import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(1)
        self.driver.find_element("id", "user-name").send_keys(username)
        time.sleep(1)
        self.driver.find_element("id", "password").send_keys(password)
        time.sleep(1)
        self.driver.find_element("id", "login-button").click()
        time.sleep(2)
