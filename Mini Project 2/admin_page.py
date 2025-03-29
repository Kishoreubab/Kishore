from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class AdminPage:
    def __init__(self, driver, new_user_credentials=None):
        self.driver = driver
        self.new_user_credentials = new_user_credentials or {
            "username": "hitman122",
            "password": "hitman122"
        }
        self.admin_button = (By.LINK_TEXT, "Admin")
        self.add_button_xpath = "//i[@class='oxd-icon bi-plus oxd-button-icon']"
        self.ess_dropdown_xpath = "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']"
        self.first_name_input_xpath = "//input[@name='firstName']"
        self.last_name_input_xpath = "//input[@name='lastName']"
        self.username_input_xpath = "//input[@name='username']"
        self.password_input_xpath = "//input[@name='password']"
        self.confirm_password_input_xpath = "//input[@name='confirmPassword']"
        self.status_dropdown_xpath = "//div[@class='oxd-select-text oxd-select-text--active']"
        self.save_button_xpath = "//button[@type='submit']"
        self.search_username_xpath = "//input[@placeholder='Search']"
        self.search_button_xpath = "//button[@type='submit']"
        self.user_row_xpath = "//div[text()='{username}']"
        self.menu_locator = "//h6[contains(text(), '{menu_name}')]"

    def admin(self):
        """Click on the Admin menu button."""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.admin_button))
        self.driver.find_element(*self.admin_button).click()

    def add(self):
        """Click on the Add button."""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.add_button_xpath)))
        self.driver.find_element(By.XPATH, self.add_button_xpath).click()

    def enabled_user(self):
        """Fill in the details for an enabled user."""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']")))
        ess_option = self.driver.find_element(By.XPATH,
                                              "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']")
        ess_option.click()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys("a").perform()
        sleep(3)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(self.new_user_credentials["username"]).perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(self.new_user_credentials["password"]).perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(self.new_user_credentials["password"]).perform()
        actions.send_keys(Keys.TAB)
        sleep(1)
        actions.send_keys(Keys.TAB)        
        actions.send_keys(Keys.ENTER).perform()
        sleep(1)


    def search_for_user(self, username):
        """Search for a user by their username."""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.search_username_xpath)))
        search_box = self.driver.find_element(By.XPATH, self.search_username_xpath)
        search_box.clear()
        search_box.send_keys(username)
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

    def verify_user_in_admin(self, username):
        """Verify if a user exists in the Admin section."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.user_row_xpath.format(username=username)))
            )
            user_row = self.driver.find_element(By.XPATH, self.user_row_xpath.format(username=username))
            print(f"User {username} exists in the records.")
            return True
        except NoSuchElementException:
            print(f"User {username} does not exist in the records.")
            return False

    def is_menu_visible_and_clickable(self, menu_name):
        """Check if the menu is visible and clickable."""
        try:
            menu_element = self.driver.find_element(By.XPATH, self.menu_locator.format(menu_name=menu_name))
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(menu_element))
            return True
        except Exception as e:
            print(f"Error while checking menu visibility/clickability: {e}")
            return False
