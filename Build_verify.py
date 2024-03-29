import time
from telnetlib import EC
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

def get_page_status_code(browser):
    current_url = browser.current_url
    response = requests.head(current_url)
    return response.status_code
# Chrome options for headless mode
chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('window-size=1920x1080')
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
    version_element = browser.find_element(By.XPATH, "//div[@aria-describedby='cdk-describedby-message-0']")
    ActionChains(browser).move_to_element(version_element).perform()

    # Execute JavaScript to retrieve the version number
    version_name = browser.execute_script("return document.querySelector('.mat-tooltip').innerText;")
    assert version_name == "BAPS MIS - V 1.0.11G"
    True
    print(version_name)

    chrome_browser.save_screenshot("screenshot.png")
    print("Screenshot saved successfully.")

    status_code = get_page_status_code(chrome_browser)
    print(f"HTTP Status Code: {status_code}")

for _, browser in browsers:
    browser.quit()
