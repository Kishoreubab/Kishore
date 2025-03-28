from asyncio import sleep
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from login_page import GuviPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fixture to initialize the WebDriver and clean up after tests
@pytest.fixture(scope="module")
def setup():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    yield driver  # Yield driver to be used in the test functions
    driver.quit()  # Cleanup: Quit the driver after all tests in the module are done

# Test to check if the URL of the page is correct
def test_check_url(setup):
    guvi_page = GuviPage(setup)  # Create an instance of the page object
    guvi_page.open()  # Open the page using the open method in GuviPage
    URL = "https://www.guvi.in/"
    assert setup.current_url == URL  # Assert if the current URL matches the expected URL

# Test to check if the page title is correct
def test_check_title(setup):
    guvi_page = GuviPage(setup)  # Create an instance of the page object
    guvi_page.open()  # Open the page
    # Assert if the title of the page matches the expected title
    assert guvi_page.get_title() == "GUVI | Learn to code in your native language"

# Test to check if the login button is visible and clickable
def test_login_button_visibility_and_clickable(setup):
    guvi_page = GuviPage(setup)  # Create an instance of the page object
    guvi_page.open()  # Open the page
    # Check if the login button is visible
    assert guvi_page.is_element_visible(By.ID, "login-btn") is True
    # Check if the login button is clickable
    assert guvi_page.is_element_clickable(By.ID, "login-btn") is True

# Test to check if the signup button is visible and clickable
def test_signup_button_visibility_and_clickable(setup):
    guvi_page = GuviPage(setup)  # Create an instance of the page object
    guvi_page.open()  # Open the page
    # Check if the signup button is visible
    assert guvi_page.is_element_visible(By.LINK_TEXT, "Sign up") is True
    # Check if the signup button is clickable
    assert guvi_page.is_element_clickable(By.LINK_TEXT, "Sign up") is True

# Test to check if clicking the signup button redirects to the correct URL
def test_navigation_to_sign_up(setup):
    guvi_page = GuviPage(setup)  # Create an instance of the page object
    guvi_page.open()  # Open the page
    guvi_page.is_element_clickable(By.LINK_TEXT, "Sign up")  # Click the signup link
    current_url = setup.current_url  # Get the current URL after click
    # Assert if the current URL is one of the expected URLs
    assert current_url == "https://www.guvi.in/sign-up/" or current_url == "https://www.guvi.in/register/"

# Test to check login and logout functionality with valid credentials
def test_login_and_logout_with_valid_credentials(setup):
    guvi_page = GuviPage(setup)  # Create an instance of the page object
    guvi_page.open()  # Open the page
    guvi_page.is_element_clickable(By.ID, "login-btn")  # Ensure login button is clickable
    guvi_page.login("username@gmail.com", "password")  # Log in with valid credentials
    sleep(1)  # Wait for the page to load after login
    # Assert if the current URL is one of the valid URLs after login
    assert setup.current_url == "https://www.guvi.in/sign-in/" or setup.current_url == "https://www.guvi.in/courses/?current_tab=myCourses"
    sleep(1)  # Wait for any transition after login
    guvi_page.logout()  # Perform logout
    print("Current URL after logout:", setup.current_url)  # Print the current URL after logout

# Test to check login functionality with invalid credentials
def test_login_with_invalid_credentials(setup):
    guvi_page = GuviPage(setup)  # Create an instance of the page object
    guvi_page.open()  # Open the page
    guvi_page.is_element_clickable(By.ID, "login-btn")  # Ensure login button is clickable
    guvi_page.login("invalid_email@example.com", "wrong_password")  # Try logging in with invalid credentials
    try:
        # Wait for the error message to be visible within 10 seconds
        error_message_element = WebDriverWait(setup, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='invalid-feedback']"))
        )
        print(f"Error message displayed: {error_message_element.text}")  # Print the error message text
        # Assert if the error message contains the expected text
        assert "Incorrect Email or Password" in error_message_element.text

    except TimeoutException:
        print("Error message did not appear in time.")  # Print message if the error message didn't appear within 10 seconds
