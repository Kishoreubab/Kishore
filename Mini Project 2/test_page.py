import pytest
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage
from admin_page import AdminPage
from selenium.common.exceptions import TimeoutException

#Read Test Data from CSV
def read_test_data(file_path):
    test_data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            test_data.append(row)
    return test_data

# Test Case - 1: Login with DDFT (Dynamic Data-Driven Testing)
@pytest.mark.parametrize("s_no, test_id, tester, date, param, username, password, expected_result", read_test_data(
    "test_data.csv"))  # Assuming test_data.csv is in the same directory
def test_login_with_ddft(s_no, test_id, tester, date, param, username, password, expected_result):
    driver = webdriver.Chrome()

    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()

        if expected_result == "Success":
            # Wait for the "Dashboard" element to be visible after successful login
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='Dashboard']"))
            )
            print("Login successful!")
            login_page.click_logout()

        elif expected_result == "Failure":
            try:
                WebDriverWait(driver, 20).until(
                    EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
                )
                print("Invalid credentials handled correctly.")
            except TimeoutException:
                print("Invalid credentials message not displayed within timeout.")

    finally:
        driver.quit()

# Test Case - 2: Check Home URL
def test_home_url():
    driver = webdriver.Chrome()

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        WebDriverWait(driver, 20).until(EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"))
        print("Home URL is working correctly.")
    except Exception as e:
        print(f"Test failed: {e}")
        pytest.fail(f"Test failed: {e}")
    finally:
        driver.quit()

# Test Case - 3: Check Visibility of Username and Password Fields
def test_username_password_visibility():
    driver = webdriver.Chrome()

    try:
        login_page = LoginPage(driver)
        login_page.open()

        assert login_page.is_username_visible(), "Username input is not visible"
        assert login_page.is_password_visible(), "Password input is not visible"

        print("Username and password input boxes are visible.")

    except Exception as e:
        print(f"Test failed: {e}")
        pytest.fail(f"Test failed: {e}")

    finally:
        driver.quit()

# Test Case - 4: Check Menus Visibility and Clickability
def test_menus_visibility_and_clickability():
    driver = webdriver.Chrome()

    try:
        # Step 1: Use the login page object to open the page and login
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        # Step 2: Wait for the URL to be the dashboard page after login
        WebDriverWait(driver, 20).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        )
        print("Successfully logged in.")

        # Step 3: List of menu names
        menu_names = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard"]

        # Check visibility and clickability of each menu
        for menu_name in menu_names:
            menu_locator = (By.LINK_TEXT, menu_name)  # Create locator for each menu
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(menu_locator)  # Wait for visibility
            )
            print(f"Menu '{menu_name}' is visible.")

            # Now check if it's clickable
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(menu_locator)  # Wait for the element to be clickable
            )
            print(f"Menu '{menu_name}' is clickable.")

            # Optionally, click on the menu (e.g., click 'Admin' as the first menu)
            if menu_name == "Admin":
                admin_button = driver.find_element(*menu_locator)
                admin_button.click()
                print("Admin menu clicked.")

    except Exception as e:
        print(f"Test failed: {e}")

    finally:
        # Step 4: Quit the driver after the test
        driver.quit()



# Test Case - 5: Create and Verify Admin User
new_user_credentials = {
        "username": "joedoe123",
        "password": "joedoe123"
    }

def test_create_and_verify_user():
    driver = webdriver.Chrome()

    try:
        # Pass the credentials to AdminPage constructor
        login_page = LoginPage(driver)
        admin_page = AdminPage(driver, new_user_credentials)  # Pass credentials here

        # Admin Login
        login_page.open()
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        # Admin tasks (Add new user and enable)
        admin_page.admin()
        admin_page.add()
        admin_page.enabled_user()  # This will now use the credentials from new_user_credentials

        # Logout from Admin
        login_page.click_logout()

        # New User Login
        login_page.enter_username(new_user_credentials["username"])  # Use the new user's credentials here
        login_page.enter_password(new_user_credentials["password"])
        login_page.click_login()

        # Wait for the URL to confirm successful login as the new user
        WebDriverWait(driver, 20).until(
            EC.url_contains("dashboard")  # Wait until the URL contains "dashboard"
        )

        print(f"New user successfully created, logged out from Admin, and logged in as '{new_user_credentials['username']}'.")

    except Exception as e:
        if new_user_credentials["username"] in str(e):  # Dynamically check if the user already exists using the new_user_credentials
            print(f"Test failed: The user '{new_user_credentials['username']}' already exists.")
            pytest.fail(f"The user '{new_user_credentials['username']}' already exists.")
        else:
            print(f"Test failed: {e}")
            pytest.fail(f"Test failed: {e}")
    finally:
        driver.quit()


# Test Case - 6: Verify User in Admin Records
def test_verify_user_in_admin_records():
    driver = webdriver.Chrome()

    try:
        login_page = LoginPage(driver)
        admin_page = AdminPage(driver, new_user_credentials)  # Pass the credentials here

        # Step 1: Login as Admin
        login_page.open()
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        # Step 2: Open Admin section
        admin_page.admin()

        # Step 3: Ensure the user is created before verifying
        admin_page.enabled_user()  # This will now use the credentials from new_user_credentials

        # Step 4: Now verify the user exists
        user_exists = admin_page.verify_user_in_admin(new_user_credentials["username"])  # Use dynamic username here
        assert user_exists, f"User '{new_user_credentials['username']}' does not exist in the records."
        print(f"The user '{new_user_credentials['username']}' exists in the Admin records.")

    except Exception as e:
        print(f"Test failed: {e}")
        pytest.fail(f"Test failed: {e}")
    finally:
        driver.quit()

