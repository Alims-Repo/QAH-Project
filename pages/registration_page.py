from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from utils.config import Config

class RegistrationPage:
    def __init__(self,driver):
        self.driver:WebDriver = driver
        self.driver.get(Config.REGISTRATION_URL)
        self.firstname_txt  = (By.ID,'input-firstname')
        self.lastname_txt = (By.ID,'input-lastname')
        self.email_txt = (By.ID,'input-email')
        self.telephone_txt = (By.ID,'input-telephone')
        self.password_txt = (By.ID,'input-password')
        self.confirm_password_txt = (By.ID,'input-confirm')
        self.yes_newsletter_radio = (By.XPATH,"//input[@name='newsletter' and @value='1']")
        self.no_newsletter_radio = (By.XPATH,"//input[@name='newsletter' and @value='0']")
        self.agree_check = (By.NAME,"agree")
        self.continue_btn = (By.XPATH,"//input[@value='Continue']")
        self.warning_alert = (By.XPATH,"//div[contains(text(),'Warning')]")

    def type_firstname(self,firstname):
        self.driver.find_element(*self.firstname_txt).send_keys(firstname)

    def type_lastname(self,lastname):
        self.driver.find_element(*self.lastname_txt).send_keys(lastname)

    def type_email(self,email):
        self.driver.find_element(*self.email_txt).send_keys(email)

    def type_telephone(self,telephone):
        self.driver.find_element(*self.telephone_txt).send_keys(telephone)

    def type_password(self,password):
        self.driver.find_element(*self.password_txt).send_keys(password)

    def type_confirm_password(self,confirm):
        self.driver.find_element(*self.confirm_password_txt).send_keys(confirm)

    def click_subscribe(self,data):
        if data=='true':
            self.click_yes_subscribe()
        else:
            self.click_no_subscribe()

    def click_yes_subscribe(self):
        self.driver.find_element(*self.yes_newsletter_radio).click()

    def click_no_subscribe(self):
        self.driver.find_element(*self.no_newsletter_radio).click()

    def click_agree(self):
        self.driver.find_element(*self.agree_check).click()

    def click_continue(self):
        self.driver.find_element(*self.continue_btn).click()


    def check_warning_exist(self):
        try:
            self.driver.find_element(*self.warning_alert).is_displayed()
        except NoSuchElementException:
            return False
        else:
            return True

