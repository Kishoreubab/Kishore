import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstagramScraper:
    def __init__(self):
        # Setup WebDriver options for Firefox
        self.firefox_options = Options()
        self.firefox_options.headless = False  # Set to False for GUI mode (True for headless mode)

        # Initialize WebDriver for Firefox
        self.driver = webdriver.Firefox(options=self.firefox_options)

    def wait_for_page_load(self):
        # Wait for the page to load and meta tags to be available.
        time.sleep(3)  # Sleep for 3 seconds (adjust as needed)
        self.wait = WebDriverWait(self.driver, 30)

    def extract_meta_tag_content(self):
        # Extract content from the meta tag.
        meta_tag = self.wait.until(EC.presence_of_element_located((By.XPATH, "//meta[@property='og:description']")))
        return meta_tag.get_attribute("content")

    def extract_counts(self, meta_content):
        # Extract followers and following counts from the meta tag content.
        followers_start = meta_content.find("Followers")
        following_start = meta_content.find("Following")

        # Extracting counts
        followers_end = meta_content.find("Following")
        following_end = meta_content.find("posts")

        followers_count = meta_content[followers_start - 5:followers_end].strip()  # Extract the followers count
        following_count = meta_content[following_start - 3:following_end].strip()  # Extract the following count

        return followers_count, following_count

    def maximize_browser(self):
        # Maximize the browser window.
        self.driver.maximize_window()

    def close_browser(self):
        # Close the browser.
        self.driver.quit()


# Initialize WebDriver
scraper = InstagramScraper()

# Navigate to the Instagram profile directly
scraper.driver.get("https://www.instagram.com/guviofficial/")

# Maximize the browser window
scraper.maximize_browser()

# Wait for the page to load
scraper.wait_for_page_load()

# Extract meta tag content
meta_content = scraper.extract_meta_tag_content()

# Extract counts from the meta content
followers_count, following_count = scraper.extract_counts(meta_content)

# Print the extracted values
print(f"Followers: {followers_count}")
print(f"Following: {following_count}")

# Close the browser after scraping
scraper.close_browser()
