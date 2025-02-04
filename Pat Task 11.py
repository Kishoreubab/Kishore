#Importing the Drivers:
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DragAndDropAutomation:
    def __init__(self):
        # Set up Chrome options
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)

        # Initialize the WebDriver with options
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()

        # Open the provided URL
        self.driver.get("https://jqueryui.com/droppable/")

    def switch_to_frame(self):
        # Wait for the page to load and the frame to be available
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

    def perform_drag_and_drop(self):
        # Locate the draggable and droppable elements
        s1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "draggable")))
        d1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "droppable")))

        # Print before performing the action
        print("Performing drag and drop action...")

        # Perform the drag and drop action
        actions = ActionChains(self.driver)
        actions.drag_and_drop(s1, d1).perform()

        # Print after performing the action
        print("Drag and drop action performed successfully!")

    def close_browser(self):
        # Wait for a while to see the result (optional)
        time.sleep(3)
        # Close the browser
        self.driver.quit()

# Example usage (you can run these manually after instantiating the class)
drag_and_drop = DragAndDropAutomation()
drag_and_drop.switch_to_frame()
drag_and_drop.perform_drag_and_drop()
drag_and_drop.close_browser()
