from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# CartPage class that provides functionality for interacting with the shopping cart
class CartPage:
    # Constructor to initialize driver and define element locators
    def __init__(self, driver):
        self.driver = driver
        # XPath for the shopping cart icon element
        self.cart_icon_xpath = "//a[@class='shopping_cart_link']"
        # XPath for the cart items
        self.cart_items_xpath = "//div[@class='cart_item']"
        # XPath for the checkout button
        self.checkout_button_xpath = "//button[@id='checkout']"
        
    # Method to navigate to the cart page by clicking the shopping cart icon
    def go_to_cart(self):
        """Click the shopping cart icon to go to the cart page."""
        # Find the cart icon using the defined XPath and click it
        cart_icon = self.driver.find_element(By.XPATH, self.cart_icon_xpath)
        cart_icon.click()

    # Method to retrieve a list of cart items (WebElements)     
    def get_cart_items(self):
        """Retrieve the list of cart items (WebElements)."""
        # Find and return all the cart items using the defined XPath
        cart_items = self.driver.find_elements(By.XPATH, self.cart_items_xpath)
        return cart_items  # Return WebElements directly

    # Method to click the checkout button and proceed to checkout
    def click_checkout_button(self):
        """Click the checkout button to proceed with checkout."""
        # Wait for the checkout button to be clickable, then click it
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout_button_xpath))
        )
        checkout_button.click()
