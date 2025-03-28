from selenium import webdriver

# WebDriverFactory class that handles the creation of WebDriver instances
class WebDriverFactory:
    # Method to get a WebDriver instance based on the specified browser name (default is "chrome")
    def get_driver(self, browser_name="chrome"):
        # If the specified browser is chrome
        if browser_name == "chrome":
            # Create ChromeOptions object to configure the Chrome WebDriver
            options = webdriver.ChromeOptions()
            # Initialize the Chrome WebDriver with the specified options
            driver = webdriver.Chrome(options=options)
        # If the browser is not Chrome, raise an exception
        else:
            raise Exception("Only Chrome is supported!")
        # Maximize the browser window for better visibility
        driver.maximize_window()
        # Return the created WebDriver instance
        return driver
