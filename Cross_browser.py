
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_browser = webdriver.Chrome()
'''fire_browser = webdriver.Firefox()
edge_browser = webdriver.Edge()'''

#browsers = [chrome_browser,fire_browser,edge_browser]
browsers = [chrome_browser]

url = "https://www.baps.org/"

for browser in browsers:
    browser.get(url)
    browser.maximize_window()
    browser.implicitly_wait(10)
    title = browser.find_element(By.XPATH,"(//a[text()='VICHARAN'])[1]")
    title_text =title.get_attribute("id")
    print(title_text)


