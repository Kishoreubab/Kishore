from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# LoginPage class that encapsulates login functionalities for the page
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.logout_button = (By.XPATH, "//a[@href='/web/index.php/auth/logout']")
        self.profile_button = (By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")

    def open(self):
        # This method opens the login page in the browser
        self.driver.get(self.url)

    def enter_username(self, username):
        # Wait until the username input field is visible, then input the provided username
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_input))
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        # Wait until the password input field is visible, then input the provided password
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input))
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        # Wait until the login button is clickable, then click it to submit the login form
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button))
        self.driver.find_element(*self.login_button).click()

    def click_logout(self):
        # Wait until the profile button is clickable, then click it to open the profile dropdown
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.profile_button))
        self.driver.find_element(*self.profile_button).click()
        # Wait until the logout button is clickable, then click it to log out
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.logout_button))
        self.driver.find_element(*self.logout_button).click()

    def is_username_visible(self):
        # Checks if the username input field is visible on the page
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_input)) is not None

    def is_password_visible(self):
        # Checks if the password input field is visible on the page
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input)) is not None
