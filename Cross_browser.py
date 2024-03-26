from selenium import webdriver
import selenium
from pages import serachPerseon_page

chrome_browser = webdriver.Chrome()
fire_browser = webdriver.Firefox()
edge_browser = webdriver.Edge()

browsers = [chrome_browser,fire_browser,edge_browser]

url = "https://dev.baps.dev/mis/"

for browser in browsers:
    browser.get(url)
