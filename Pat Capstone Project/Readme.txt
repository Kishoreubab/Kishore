# Python Selenium Automation for SauceDemo Web Application

## Project Overview
This project automates the **SauceDemo** e-commerce website (https://www.saucedemo.com/) using **Python Selenium** and **Pytest** framework. The goal of this project is to verify the functionality of various features on the site, including login, product selection, cart functionality, checkout, and order confirmation. We use **Page Object Model (POM)** and **Data-Driven Testing Framework (DDTF)** in the project.

The automation also generates **Pytest HTML reports** to provide detailed insights into the test results.

## Tools Used
- Python 3.x
- Selenium WebDriver
- Pytest Framework
- Excel (for Data-Driven Testing)
- Page Object Model (POM)
- Pytest HTML Reports
- Explicit Waits (Mandatory)

## Test Suite
The test suite consists of the following test cases:

### Test-Case-1: Login Testing with Multiple Users
1. Test login with different usernames: `standard_user`, `problem_user`, `performance_glitch_user`, and `locked_out_user` using the password `secret_sauce`.
2. Test login using cookies without using URL or Page-Title.
3. Generate Pytest-based HTML reports for the tests.

### Test-Case-2: Login with Invalid User
1. Test login with `guvi_user` and password `Secret@123`.
2. Generate Pytest-based HTML reports for the test.

### Test-Case-3: Logout Functionality
1. Test whether the logout button is functioning correctly.
2. Check the visibility of the logout button.
3. Generate Pytest-based HTML reports for the tests.

### Test-Case-4: Cart Button Visibility
1. Verify the visibility of the Cart button.
2. Generate Pytest-based HTML reports for the test.

### Test-Case-5: Random Product Selection
1. Randomly select four products out of six available products.
2. Fetch and display the name and price of the selected products.
3. Generate Pytest-based HTML reports for the tests.

### Test-Case-6: Add Products to Cart
1. Randomly select four products out of six available products.
2. Add the selected products to the cart.
3. Verify that the cart displays the four products.
4. Generate Pytest-based HTML reports for the tests.

### Test-Case-7: Cart Verification
1. Click the Cart button and verify the products added to the cart.
2. Fetch the product details from the cart.
3. Generate Pytest-based HTML reports for the tests.

### Test-Case-8: Checkout Process
1. Click the Checkout button and input details like First Name, Last Name, and Pin Code.
2. Take a screenshot of the Checkout Overview page.
3. Verify that the products and details on the Checkout page match the items added to the cart.
4. Click the Finish button and confirm the action.
5. Generate Pytest-based HTML reports for the tests.

## Precondition
- The test cases include both positive and negative scenarios.
- Excel or CSV files are used for **Data-Driven Testing Framework (DDTF)** to provide input test data.
- **Python OOP** and **Exception Handling** are used in the test scripts.
- **Page Object Model (POM)** is used to organize code and encapsulate page interactions.
- **Explicit Waits** are used throughout the tests to ensure elements are interactable.

## Installation
1. Install the required dependencies:
    ```bash
    pip install selenium pytest openpyxl
    ```

/python-selenium-automation
│
├── /PAT_Capstone_Project     # Main project folder
│   ├── test_page.py          # Test case file for testing functionality
│   ├── product_page.py       # Page object file for product page interactions
│   ├── path.py               # Page object file for login page interactions (could be renamed to login_page.py)
│   ├── browser_page.py       # Utility file for browser functions
│   ├── cart_page.py          # Page object file for cart interactions
│   └── checkout_page.py      # Page object file for checkout interactions


## Code Guidelines
- **Object-Oriented Programming (OOP)**: The code uses Python OOP principles for better organization and maintainability.
- **Page Object Model (POM)**: Each page interaction is encapsulated in its own class, following the POM design pattern for reusability and maintainability.
- **Explicit Waits**: Explicit waits are used to ensure that elements are loaded before interacting with them.
- **Data-Driven Testing Framework (DDTF)**: Test data is provided through Excel files to execute tests with multiple data sets.
- **Pytest HTML Reports**: Pytest is used to run the tests, and HTML reports are generated for test results.
