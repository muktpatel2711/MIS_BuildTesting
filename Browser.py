from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Trying to locate an element that doesn't exist
    element = driver.find_element_by_id("nonexistent_id")
    print("Element found:", element)
except NoSuchElementException as e:
    print("Element not found. Exception:", e)

# Close the browser
driver.quit()
