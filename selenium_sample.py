from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.options import Options

# Initialize the WebDriver (e.g., Chrome)
chrome_options = Options()
driver = webdriver.Firefox(options=chrome_options)

# Open the target URL
driver.get('https://diskominfo.acehprov.go.id/halaman/sop-bencana')

# Wait for JavaScript to load the dynamic content
time.sleep(5)  # Adjust based on the page's load time

# Extract links using Selenium
links = driver.find_elements(By.XPATH, "//a[@href]")
urls = [link.get_attribute('href') for link in links]

# Print extracted URLs
for url in urls:
    print(url)

# Close the WebDriver
driver.quit()

