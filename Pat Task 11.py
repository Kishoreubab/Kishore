#Importing the Drivers
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")

# Wait for the page to load and frame to be available
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

# Locate the draggable and droppable elements
s1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "draggable")))
d1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "droppable")))

# Perform drag and drop action
actions = ActionChains(driver)
actions.drag_and_drop(s1, d1).perform()

# Wait for a while to see the result (optional)
time.sleep(5)

# Close the browser
driver.quit()
