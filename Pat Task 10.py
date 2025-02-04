import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the Instagram profile
driver.get("https://www.instagram.com/guviofficial/")

# Add a sleep time to ensure the page has time to load
time.sleep(3)  # Sleep for 3 seconds (adjust as needed)

# Create WebDriverWait
wait = WebDriverWait(driver, 30)

# Wait for the page to load and the `meta` tag to be available
meta_tag = wait.until(EC.presence_of_element_located((By.XPATH, "//meta[@property='og:description']")))

# Extract the content from the `meta` tag
meta_content = meta_tag.get_attribute("content")

# Extract followers and following from the content string
followers_start = meta_content.find("Followers")  # Find position of "Followers"
following_start = meta_content.find("Following")  # Find position of "Following"

# Extracting counts
followers_end = meta_content.find("Following")  # The end position of followers count
following_end = meta_content.find("posts")  # The end position of following count

followers_count = meta_content[followers_start - 5:followers_end].strip()  # Extract the followers count
following_count = meta_content[following_start - 3:following_end].strip()  # Extract the following count

# Print the extracted values
print(f"Followers: {followers_count}")
print(f"Following: {following_count}")

# Close the browser after scraping
driver.quit()
