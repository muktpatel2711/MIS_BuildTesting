
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestLoginPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
    def url(self):
        self.driver.get("http://bapsausmisadminwebapp.dev.kcspl.in:9090/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(25)


    def sso(self):
        self.driver.find_element(By.NAME,"submit").click()

    def login(self):
        self.driver.find_element(By.NAME,"userName").send_keys("mihir")
        self.driver.find_element(By.NAME, "password").send_keys("Test@123")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-submit']").click()

    def position(self):
        self.driver.find_element(By.XPATH, "//button[text()='North America System Admin']").click()
    def manageperson(self):
        manageperson = self.driver.find_element(By.XPATH, "(//span[normalize-space()='Manage Person'])[1]")
        action_chains =ActionChains(self.driver)
        time.sleep(5)
        action_chains.move_to_element(manageperson).click().perform()
        time.sleep(2)

    def serachperson(self):
        searchperson = self.driver.find_element(By.XPATH, "(//span[normalize-space()='Search Person'])[1]")
        action_chains =ActionChains(self.driver)
        time.sleep(5)
        action_chains.move_to_element(searchperson).click().perform()
        time.sleep(2)

    def AddressChanges(self):
        bapsid =self.driver.find_element(By.XPATH,"// input[ @ formcontrolname = 'BAPSId']")
        bapsid.send_keys("17")
        bapsid.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//button[@class='single-icon mr-1 mb-1 ng-star-inserted'])[1]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//strong[text()=' Address ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[text()='Generate Link']").click()

    def address_form(self):
        try:
            expiredDate = self.driver.find_element(By.XPATH,"//input[@ formcontrolname='expiryDate']")
            e_text = expiredDate.get_attribute("XPATH")
            print(e_text)
            date = self.driver.find_element(By.XPATH,"(//button[@class='mat-icon-button mat-button-base'])[2]")
            date.click()
            select_date = self.driver.find_element(By.XPATH,"//div[text()='18']")
            select_date.click()
        except:
            print("Expired date already set")
        try:
            resend = self.driver.find_element(By.XPATH,"//button[text()='Resend']")
            resend.click()
            time.sleep(5)
        except:
            send = self.driver.find_element(By.XPATH, "//button[text()='Send']")
            send.click()
            time.sleep(5)

    def openEmail(self):
        self.driver.get("https://yopmail.com/wm")
        login_yopmail = self.driver.find_element(By.ID,"login")
        login_yopmail.send_keys("vinsh105")
        login_yopmail.send_keys(Keys.ENTER)
        email_link = self.driver.find_element(By.XPATH,"//div[@class='ellipsis nw b f18']")
        print(email_link.text)
        self.driver.back()
        time.sleep(5)

    def signIn(self):
        self.url()
        self.sso()
        self.login()
        self.position()
        self.manageperson()
        self.serachperson()
        self.AddressChanges()
        self.address_form()
        self.take_screenshot()
        self.openEmail()
        self.tearDown()

    def take_screenshot(self, filename="Successfully.png"):
        self.driver.save_screenshot(filename)

    def tearDown(self):
        self.driver.quit()

login = TestLoginPage()
login.signIn()

