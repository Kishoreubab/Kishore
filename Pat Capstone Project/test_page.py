import csv
import random
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from browser_page import BrowserPage
from cart_page import CartPage
from path import LoginPage
from product_page import ProductPage

# Load the user data from the CSV file
def load_user_data_from_csv(file_path):
    user_data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        # Loop through each row and filter out specific usernames
        for row in csv_reader:
            if row['username'] in ['standard_user', 'problem_user', 'performance_glitch_user', 'locked_out_user']:
                user_data.append((row['username'], row['password']))  # Append valid users and passwords
    return user_data

# Load the user data from the CSV file
user_data = load_user_data_from_csv("user_data.csv")


# Test Case - 1: Testing login and login using cookies
@pytest.mark.parametrize("username, password", user_data)
def test_login_and_login_using_cookies(username, password):
    url = "https://www.saucedemo.com/"  # URL for the application
    browser = BrowserPage(url)  # Initialize the browser page
    driver = browser.get_driver()  # Get the WebDriver instance

    # Initialize LoginPage to perform login actions
    login_page = LoginPage(driver)
    login_page.login(username, password)  # Login with the provided username and password

    time.sleep(3)  # Adding sleep for simplicity, but it's recommended to use WebDriverWait instead for reliability

    try:
        # Check if the inventory page is displayed after login
        inventory_element = driver.find_element(By.ID, 'inventory_container')
        if inventory_element.is_displayed():
            print(f"Login successful for user: {username}")
        else:
            print(f"Login failed for user: {username}")
    except Exception as e:
        print(f"Login failed for user {username}: {str(e)}")

    # Store the cookies after a successful login for session reuse
    cookies = driver.get_cookies()
    driver.get(url)  # Reload the page to start a new session

    # Add previously stored cookies back to the new session
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

    time.sleep(3)  # Wait for the page to reload

    try:
        # Check if the inventory page is displayed after logging in using cookies
        inventory_element = driver.find_element(By.ID, 'inventory_container')
        if inventory_element.is_displayed():
            print(f"Login using cookies was successful for user: {username}")
        else:
            print(f"Login using cookies failed for user: {username}")
    except Exception as e:
        print(f"Login using cookies failed for user {username}: {str(e)}")

    # Close the browser after the test
    browser.quit_browser()


# Test Case - 2: Testing login for a user who will fail the login (guvi_user)
def test_login_guvi_user():
    url = "https://www.saucedemo.com/"  # URL for the application
    browser = BrowserPage(url)  # Initialize the browser page
    driver = browser.get_driver()  # Get the WebDriver instance

    username = "guvi_user"  # Invalid username for login
    password = "Secret@123"  # Password for the invalid user
    login_page = LoginPage(driver)  # Initialize the LoginPage object

    try:
        login_page.login(username, password)  # Try logging in with the invalid user credentials

        # Wait for and check the error message container
        error_message_container = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.error-message-container.error'))
        )
        assert error_message_container.is_displayed(), "Error message container not displayed"
        print("Test Passed: Error message displayed successfully.")

    except Exception as e:
        print(f"Test failed: {str(e)}")
        assert False, f"Login failed: {str(e)}"

    finally:
        # Ensure the driver quits after the test
        browser.quit_browser()


# Test Case - 3: Testing logout functionality and visibility
def test_logout_functionality_and_visibility():
    url = "https://www.saucedemo.com/"  # URL for the application
    browser = BrowserPage(url)  # Initialize the browser page
    driver = browser.get_driver()  # Get the WebDriver instance

    username = "standard_user"  # Valid username for login
    password = "secret_sauce"  # Valid password for login

    login_page = LoginPage(driver)  # Initialize the LoginPage object
    login_page.login(username, password)  # Login with the valid user credentials

    login_page.logout()  # Perform logout action

    logout_button = driver.find_element(By.ID, 'login-button')  # Find logout button

    assert logout_button.is_displayed(), "Logout button is not visible"  # Ensure the logout button is visible
    assert driver.current_url == url, "User is not redirected to the login page after logout"  # Ensure correct URL after logout

    # Close the browser after the test
    browser.quit_browser()


# Test Case - 4: Testing cart button visibility after login
def test_cart_button_visibility():
    url = "https://www.saucedemo.com/"  # URL for the application
    browser = BrowserPage(url)  # Initialize the browser page
    driver = browser.get_driver()  # Get the WebDriver instance

    username = "standard_user"  # Valid username for login
    password = "secret_sauce"  # Valid password for login

    login_page = LoginPage(driver)  # Initialize the LoginPage object
    login_page.login(username, password)  # Login with the valid user credentials

    # Check if the cart button is visible on the page
    cart_button = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    assert cart_button.is_displayed(), "Cart button is not visible"  # Ensure the cart button is visible

    # Close the browser after the test
    browser.quit_browser()


# Test Case - 5: Testing selecting random products from the inventory
def test_select_random_products():
    url = "https://www.saucedemo.com/"  # URL for the application
    browser = BrowserPage(url)  # Initialize the browser page
    driver = browser.get_driver()  # Get the WebDriver instance

    username = "standard_user"  # Valid username for login
    password = "secret_sauce"  # Valid password for login

    login_page = LoginPage(driver)  # Initialize the LoginPage object
    login_page.login(username, password)  # Login with the valid user credentials

    product_page = ProductPage(driver)  # Initialize the ProductPage object

    # Get all products available in the inventory
    all_products = product_page.get_all_products()

    # Check if there are exactly 6 products available
    assert len(all_products) == 6, f"Expected 6 products, found {len(all_products)}"

    # Select 4 random products from the 6 available products
    selected_products = random.sample(all_products, 4)

    for product in selected_products:
        product_name = product_page.get_product_name(product)
        product_price = product_page.get_product_price(product)
        print(f"Product Name: {product_name}, Price: {product_price}")

    assert len(selected_products) == 4, "Less than 4 products were selected."  # Ensure exactly 4 products were selected

    # Close the browser after the test
    browser.quit_browser()


# Test Case - 6, 7 & 8: Testing adding, verifying, and checking out products in the cart
def test_select_add_and_verify_products_in_cart_checkout_and_logout():
    username = "standard_user"  # Valid username for login
    password = "secret_sauce"  # Valid password for login

    # Initialize the browser using BrowserPage
    browser_page = BrowserPage()  # Initialize the browser page
    driver = browser_page.get_driver()  # Get the WebDriver instance

    try:
        # Step 1: Login to the application
        login_page = LoginPage(driver)
        login_page.login(username, password)  # Perform login with valid credentials

        # Step 2: Add 4 random products to the cart
        product_page = ProductPage(driver)
        all_products = product_page.get_all_products()

        assert len(all_products) == 6  # Ensure there are 6 products available

        selected_products = random.sample(all_products, 4)

        # Add selected products to the cart
        for product in selected_products:
            product_page.add_to_cart(product)

        # Ensure that the cart has the correct number of items (4)
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "shopping_cart_badge"), "4"
            )
        )

        # Step 3: Navigate to the cart page
        cart_page = CartPage(driver)
        cart_page.go_to_cart()

        # Step 4: Verify that there are products in the cart
        cart_items = cart_page.get_cart_items()
        assert len(cart_items) == 4, f"Expected 4 products in cart, but found {len(cart_items)}"

        # Fetch the product details (name and price) from each cart item
        cart_product_details = []
        for cart_item in cart_items:
            cart_item_name = cart_item.find_element(By.XPATH, ".//div[@class='inventory_item_name']").text
            cart_item_price = cart_item.find_element(By.XPATH, ".//div[@class='inventory_item_price']").text
            cart_product_details.append({"name": cart_item_name, "price": cart_item_price})
            print(f"Product Name: {cart_item_name}, Product Price: {cart_item_price}")

        print("Test Passed: Products in the cart fetched successfully.")

        # Step 5: Proceed to checkout
        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']"))
        )
        checkout_button.click()

        # Fill in customer details (first name, last name, and zip code)
        first_name_input = driver.find_element(By.XPATH, "//input[@id='first-name']")
        last_name_input = driver.find_element(By.XPATH, "//input[@id='last-name']")
        zip_code_input = driver.find_element(By.XPATH, "//input[@id='postal-code']")

        first_name_input.send_keys("John")
        last_name_input.send_keys("Doe")
        zip_code_input.send_keys("12345")

        # Click the Continue button
        continue_button = driver.find_element(By.XPATH, "//input[@type='submit']")
        continue_button.click()

        # Step 6: Verify product details on the Checkout Overview page
        checkout_items = driver.find_elements(By.XPATH, "//div[@class='cart_item']")
        assert len(checkout_items) == 4, f"Expected 4 items on Checkout Overview, found {len(checkout_items)}"

        # Verify that the products in the cart match those on the checkout page
        for idx, checkout_item in enumerate(checkout_items):
            checkout_item_name = checkout_item.find_element(By.XPATH, ".//div[@class='inventory_item_name']").text
            checkout_item_price = checkout_item.find_element(By.XPATH, ".//div[@class='inventory_item_price']").text
            assert checkout_item_name == cart_product_details[idx][
                "name"], f"Product names don't match for {checkout_item_name}"
            assert checkout_item_price == cart_product_details[idx][
                "price"], f"Product prices don't match for {checkout_item_name}"
            print(f"Checkout Product Name: {checkout_item_name}, Checkout Product Price: {checkout_item_price}")

        print("Test Passed: Checkout Overview verified successfully.")

        # Step 7: Take a screenshot of the Checkout Overview
        screenshot_path = r"C:\Users\HP\PycharmProjects\PythonProject\Pat_Selenium_Project\PAT_Capstone_Project\checkout_overview.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")

        # Step 8: Press the Finish Button and get the confirmation
        finish_button = driver.find_element(By.XPATH, "//button[@id='finish']")
        finish_button.click()

        # Step 9: Confirm the action (you can confirm the success message or URL)
        confirmation_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[@class='complete-header' and text()='Thank you for your order!']"))
        )
        assert confirmation_message.is_displayed(), "Order confirmation message not found."
        print("Test Passed: Order confirmed successfully.")

        # Step 10: Logout after test
        logout_button = driver.find_element(By.XPATH, "//button[@id='logout_sidebar_link']")
        logout_button.click()
        print("Test Passed: Logged out successfully.")

    except Exception as e:
        print(f"Test failed: {str(e)}")
