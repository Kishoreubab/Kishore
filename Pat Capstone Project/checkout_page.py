from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_items_xpath = "//div[@class='cart_item']"  # XPath for checkout items
        self.first_name_input_id = "first-name"
        self.last_name_input_id = "last-name"
        self.postal_code_input_id = "postal-code"
        self.continue_button_xpath = "//input[@value='Continue']"
        self.checkout_overview_xpath = "//div[@class='checkout_summary_container']"  # Optional: to validate if checkout page is loaded

    def get_checkout_items(self):
        """Get all items in the checkout overview."""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.checkout_items_xpath))
        )

    def enter_personal_details(self, first_name, last_name, postal_code):
        """Enter personal details in the checkout form."""
        self.driver.find_element(By.ID, self.first_name_input_id).send_keys(first_name)
        self.driver.find_element(By.ID, self.last_name_input_id).send_keys(last_name)
        self.driver.find_element(By.ID, self.postal_code_input_id).send_keys(postal_code)

    def click_continue_button(self):
        """Click the continue button on the checkout page."""
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_button_xpath))
        )
        continue_button.click()

    def enter_checkout_info(self, first_name, last_name, postal_code):
        """Enter the checkout info (this method is optional and can be removed as it's redundant)."""
        self.enter_personal_details(first_name, last_name, postal_code)  # Calls enter_personal_details
        self.click_continue_button()  # Optionally click continue after entering details
