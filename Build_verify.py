from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

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
    print(f"Successfully navigated to {url} in {browser_name} browser")


for _, browser in browsers:
    browser.quit()
