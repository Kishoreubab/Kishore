# Python Selenium Automation for OrangeHRM Web Application

## Project Overview
This project automates the OrangeHRM web application (https://opensource-demo.orangehrmlive.com/web/index.php/auth/login) using the Python Selenium framework. The objective is to automate various test cases that verify the functionality of the web application. This includes login, menu visibility, user creation, and verifying successful login with valid and invalid credentials.

The project follows the **Page Object Model (POM)** design pattern, uses **Data Driven Testing Framework (DDTF)** with Excel for test data, and generates **Pytest HTML reports** for test results.

## Tools Used
- Python 3.x
- Selenium WebDriver
- Pytest Framework
- Excel (for Data-Driven Testing)
- Page Object Model (POM) design pattern
- Pytest HTML Reports
- Explicit Waits (Mandatory)

## Test Suite
The test suite includes the following test cases:

### Test-Case-1: Login Testing with DDT
1. Create an Excel file with usernames and passwords.
2. Using DDT, verify whether the login is successful with each username and password. After a successful login, logout from the CRM.
3. Verify login using cookies.
4. Generate Pytest-based HTML reports for these tests.

### Test-Case-2: Verify Home URL
1. Verify if the home URL (https://opensource-demo.orangehrmlive.com/web/index.php/auth/login) is working correctly.
2. Generate Pytest-based HTML reports for the test.

### Test-Case-3: Verify Login Form Visibility
1. Verify whether the username and password input fields are visible on the login page.
2. Generate Pytest-based HTML reports for this test.

### Test-Case-4: Verify Menus after Login
1. After a successful login, verify whether the following menus are visible and clickable: 
   - Admin
   - PIM
   - Leave
   - Time
   - Recruitment
   - My Info
   - Performance
   - Dashboard
2. Generate Pytest-based HTML reports for this test.

### Test-Case-5: Create New User
1. Create a new user from the Admin menu and verify whether the newly created user can log into the CRM successfully.
2. Generate Pytest-based HTML reports for this test.

### Test-Case-6: Verify New User in Admin Records
1. From the Admin menu, verify if the newly created user exists in the user records.
2. Generate Pytest-based HTML reports for this test.

## Precondition
- The test cases include both positive and negative scenarios.
- You need to have an Excel file for Data Driven Testing (DDT) with valid login credentials and other test data.
- You need to use the Page Object Model (POM) design pattern for all test automation.

## Installation
1. Install the required dependencies:
    ```bash
    pip install selenium pytest openpyxl
    ```

/python-selenium-automation
│
/mini_project2
│
├── test_page.py            # Test case file for testing functionality
├── admin_page.py           # Page object file for admin page interactions
├── login_page.py           # Page object file for login page interactions
└── utils.py                # Utility file for browser functions

 
## Usage
1. Navigate to the project directory.
2. Run the tests using Pytest:
    ```bash
    pytest --html=report.html --maxfail=1 --disable-warnings
    ```

## Code Guidelines
- **OOP (Object-Oriented Programming)**: Python OOP principles are followed for better structure and maintainability.
- **POM (Page Object Model)**: Each page interaction is encapsulated in a separate class for modularity and reusability.
- **DDTF (Data Driven Testing Framework)**: Test data is stored in Excel files and is used to execute tests with different data sets.
- **Explicit Waits**: Explicit waits are used to ensure the elements are loaded before interacting with them.
- **Pytest HTML Reports**: HTML reports are generated to show the result of the automation tests.
