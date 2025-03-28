from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


# ProductPage class that provides functionality for interacting with product elements
class ProductPage:
    
    # Constructor to initialize driver and define element locators for product details
    def __init__(self, driver):
        self.driver = driver
        # XPath for the individual product container
        self.product_xpath = "//div[@class='inventory_item']"
        # XPath for the product name within the product container
        self.product_name_xpath = ".//div[@class='inventory_item_name ']"
        # XPath for the product price within the product container
        self.product_price_xpath = ".//div[@class='inventory_item_price']"
        # XPath for the "Add to Cart" button within the product container
        self.add_to_cart_button_xpath = ".//button[contains(text(),'Add to cart')]"

    # Method to get a list of all products on the product page
    def get_all_products(self):
        try:
            # Wait until all product elements are present on the page, then return them
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, self.product_xpath))
            )
            return self.driver.find_elements(By.XPATH, self.product_xpath)
        except StaleElementReferenceException:
            # Retry getting products if there was a stale element reference exception
            return self.get_all_products()

    # Method to get the name of a specific product
    def get_product_name(self, product):
        try:
            # Find the product name within the given product element and return the text
            return product.find_element(By.XPATH, self.product_name_xpath).text
        except StaleElementReferenceException:
            # Retry getting the product name if there was a stale element reference exception
            return self.get_product_name(product)

    # Method to get the price of a specific product
    def get_product_price(self, product):
        try:
            # Find the product price within the given product element and return the text
            return product.find_element(By.XPATH, self.product_price_xpath).text
        except StaleElementReferenceException:
            # Retry getting the product price if there was a stale element reference exception
            return self.get_product_price(product)

    # Method to add a specific product to the cart by clicking the "Add to Cart" button
    def add_to_cart(self, product):
        try:
            # Find the "Add to Cart" button within the given product element and click it
            add_to_cart_button = product.find_element(By.XPATH, self.add_to_cart_button_xpath)
            add_to_cart_button.click()
        except StaleElementReferenceException:
            # Retry clicking the "Add to Cart" button if there was a stale element reference exception
            self.add_to_cart(product)
