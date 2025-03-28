from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class DriverFactory:
    def __init__(self):# Constructor to initialize the driver options
        self.options = Options()# Create an instance of ChromeOptions
        self.options.add_argument("--headless")

    def get_driver(self):
        # Initialize Chrome driver with options
        return webdriver.Chrome(options=self.options)
