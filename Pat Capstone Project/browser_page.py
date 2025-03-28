from selenium import webdriver

class BrowserPage:
    def __init__(self, url="https://www.saucedemo.com/"):
        """Initialize the browser and open the specified URL."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)  # Open the URL passed to the constructor

    def quit_browser(self):
        """Quit the browser after the test is complete."""
        self.driver.quit()

    def get_driver(self):
        """Return the current driver instance."""
        return self.driver
