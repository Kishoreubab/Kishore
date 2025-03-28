from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# LoginPage class that encapsulates login and logout functionality
class LoginPage:
    
    # Constructor to initialize driver and define element locators for login and logout
    def __init__(self, driver):
        self.driver = driver
        # ID locators for username, password, and login button
        self.username_id = "user-name"
        self.password_id = "password"
        self.login_button_id = "login-button"
        # ID locators for the burger menu button and logout link
        self.burger_menu_id = "react-burger-menu-btn"
        self.logout_link_id = "logout_sidebar_link"

    # Method to enter the username in the username field
    def enter_username(self, username):
        try:
            # Wait until the username field is present, then input the provided username
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.username_id))
            )
            username_field.send_keys(username)
        except Exception as e:
            # Print an error message if there's an issue with entering the username
            print(f"Error entering username: {str(e)}")

    # Method to enter the password in the password field
    def enter_password(self, password):
        try:
            # Wait until the password field is present, then input the provided password
            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.password_id))
            )
            password_field.send_keys(password)
        except Exception as e:
            # Print an error message if there's an issue with entering the password
            print(f"Error entering password: {str(e)}")

    # Method to click the login button to submit the login form
    def click_login(self):
        try:
            # Wait until the login button is clickable, then click it
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, self.login_button_id))
            )
            login_button.click()
        except Exception as e:
            # Print an error message if there's an issue clicking the login button
            print(f"Error clicking login button: {str(e)}")

    # Method to perform login by entering the username, password, and clicking the login button
    def login(self, username, password):
        # Call the methods to enter the username and password, and click login
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # Method to log out by clicking the burger menu and the logout link
    def logout(self):
        try:
            # Wait until the burger menu button is clickable, then click it
            burger_menu_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, self.burger_menu_id))
            )
            burger_menu_button.click()

            # Wait until the logout link is clickable, then click it
            logout_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, self.logout_link_id))
            )
            logout_button.click()
        except Exception as e:
            # Print an error message if there's an issue during the logout process
            print(f"Error during logout: {str(e)}")

