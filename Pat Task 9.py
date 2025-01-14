from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

import time

# Set up the WebDriver (Make sure the path to chromedriver is correct or set it in your PATH)
driver = webdriver.Chrome()

# Open the URL
url = "https://www.saucedemo.com/"
driver.get(url)

# Maximize the window (optional)
driver.maximize_window()

# Locate the Username field and input the Username
webelement_of_email_input = driver.find_element(By.ID,"user-name")
webelement_of_email_input.send_keys("standard_user")
    
# Locate the Password field and input the Password
webelement_of_password_input = driver.find_element(By.ID,"password")
webelement_of_password_input.send_keys("secret_sauce")

# Locate and click the Login button
login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
login_button.click()

# Wait for the page to load completely
sleep(3)

# 1) Fetch the title of the webpage
print(driver.title) 

# 2) Fetch the current URL of the webpage
print(driver.current_url)

# 3) Extract the entire contents of the webpage
print(driver.page_source)

# Save the contents into a text file
file = open("Webpage_task_11.txt", "w", encoding="utf-8")
file.write(driver.page_source)
file.close()

print("Webpage contents saved to 'Webpage_task_11.txt'")

# Close the browser after the task is complete
driver.quit()

