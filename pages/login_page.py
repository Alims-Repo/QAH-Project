from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.config import Config

class LoginPage:
    def __init__(self,driver:WebDriver):
        self.driver:WebDriver = driver
        self.driver.get(Config.LOGIN_URL)
        self.email_txt = (By.NAME,"email")
        self.password_txt = (By.NAME,"password")
        self.login_btn = (By.XPATH,"//input[@value='Login']")

    def type_email(self,email):
        self.driver.find_element(*self.email_txt).send_keys(email)

    def type_password(self,password):
        self.driver.find_element(*self.password_txt).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()