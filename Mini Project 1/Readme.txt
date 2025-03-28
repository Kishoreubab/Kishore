# Python Selenium Automation for GUVI Web Application

## Project Overview
This project automates the GUVI web application (https://www.guvi.in) using the Python Selenium framework. The primary objective is to automate the testing of various user interactions with the website, including validation of the URL, title, login, sign-up, and login/logout functionality.

## Tools Used
- Python 3.x
- Selenium WebDriver
- Pytest Framework
- WebDriver: Chrome/Edge/Firefox

## Test Suite
The test suite consists of 7 test cases:
1. **Test URL Validity**: Checks if the website URL is valid.
2. **Test Page Title**: Verifies the page title is correct.
3. **Login Button**: Verifies visibility and clickability of the Login button.
4. **Sign-Up Button**: Verifies visibility and clickability of the Sign-Up button.
5. **Sign-Up Page Navigation**: Verifies the navigation to the Sign-Up page.
6. **Login & Logout**: Verifies successful login and logout.
7. **Invalid Login**: Verifies error message on invalid login credentials.

## Precondition
- The test cases contain both positive and negative scenarios.
- Valid test data (email, password) is required for login verification.

## Installation
1. Install the required dependencies:
    ```bash
    pip install selenium pytest
    ```
/python-selenium-automation
│
├── /mini_project               # Folder containing the main project files
│   ├── base_page.py            # Base page class with common functionalities
│   ├── login_page.py           # Login page class for login functionalities
│   └── test_page.py            # Test cases for testing the pages

## Usage
1. Navigate to the project directory.
2. Run the test suite with:
    ```bash
    pytest test_guvi.py
    ```
## Code Guidelines
- **Object-Oriented Programming (OOP)**: Python OOP concepts are used.
- **Exception Handling**: Proper exception handling for stability.
- **Comments**: Adequate comments explaining the code.
- **PyLint**: Code follows PyLint guidelines for readability.
