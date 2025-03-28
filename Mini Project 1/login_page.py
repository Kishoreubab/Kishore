from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class GuviPage:
    def __init__(self, driver):
        # Constructor to initialize the WebDriver instance
        self.driver = driver

    def open(self):
        # Opens the Guvi website
        self.driver.get("https://www.guvi.in")

    def get_title(self):
        # Returns the title of the current page
        return self.driver.title

    def is_element_visible(self, by, value):
        # Checks if an element is visible on the page
        try:
            # Try to find the element using the provided 'by' locator and 'value'
            element = self.driver.find_element(by, value)
            return element.is_displayed()  # Returns True if the element is visible, otherwise False
        except:
            # If the element is not found or there is an exception, return False
            return False

    def is_element_clickable(self, by, value):
        # Checks if an element is clickable and attempts to click it
        try:
            # Try to find the element using the provided 'by' locator and 'value'
            element = self.driver.find_element(by, value)
            element.click()  # Click the element if it's found
            return True  # Return True if the element was clicked successfully
        except:
            # If the element is not found or the click operation fails, return False
            return False

    def login(self, email, password):
        # Method to log into the website with the provided email and password
        # Locate the email input field and enter the provided email
        self.driver.find_element(By.ID, "email").send_keys(email)
        # Locate the password input field and enter the provided password
        self.driver.find_element(By.ID, "password").send_keys(password)
        # Locate the login button and click to submit the login form
        self.driver.find_element(By.ID, "login-btn").click()

    def logout(self):
        # Method to log out from the account
        actions = ActionChains(self.driver)
        # Perform a series of TAB key presses to navigate to the profile dropdown
        actions.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).perform()

        # Wait for the profile dropdown button (with id="dropdown_title") to be clickable
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "dropdown_title")))

        try:
            # Find the profile dropdown button and click it to reveal the options
            profile_dropdown = self.driver.find_element(By.ID, "dropdown_title")
            profile_dropdown.click()

            # Wait for the "Sign Out" option (inside the dropdown) to be clickable
            sign_out_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='dropdown_contents' and text()='Sign Out']"))
            )

            # Scroll the page to bring the Sign Out button into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", sign_out_button)

            # Click the "Sign Out" button
            sign_out_button.click()

        except Exception as e:
            # Catch any exceptions that occur and print error messages
            print("Error: Unable to click on the Sign Out button.")
            print(str(e))

    def navigate_to_sign_in(self):
        # Navigate to the Sign In page by clicking the "Sign In" link
        self.driver.find_element(By.LINK_TEXT, "Sign In").click()
