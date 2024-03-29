import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

# Chrome options for headless mode
chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
#firefox_options = FirefoxOptions()
#firefox_options.headless = True

chrome_browser = webdriver.Chrome(options=chrome_options)
#firefox_browser = webdriver.Firefox(options=firefox_options)
browsers = [('Chrome', chrome_browser)]
#browsers = [('Chrome', chrome_browser), ('Firefox', firefox_browser)]
url = "https://dev.baps.dev/mis/"

for browser_name, browser in browsers:
    browser.get(url)
    browser.implicitly_wait(10)
    browser.maximize_window()
    print(f"Successfully navigated to {url} in {browser_name} browser")
    browser.find_element(By.XPATH, "//input[@class='login-btn']").click()
    browser.find_element(By.NAME, "userName").send_keys("contactvpatel@gmail.com")
    browser.find_element(By.NAME, "password").send_keys("Baps@123")
    browser.find_element(By.XPATH,"//button[@class='btn btn-primary btn-submit']").click()
    browser.find_element(By.XPATH,"//button[text()='North America System Admin']").click()
    time.sleep(5)
    hover_element = browser.find_element(By.XPATH, "// div[normalize - space() = 'V 1.0.11']")
    # Wait for the version element to be visible
    version_element = hover_element.text

    # If version element found, print its text
    if version_element:
        version_name = version_element
        print(f"Version Name: {version_name}")
    else:
        print("Version name not found.")



    chrome_browser.save_screenshot("screenshot.png")
    print("Screenshot saved successfully.")




for _, browser in browsers:
    browser.quit()
