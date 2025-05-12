from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.config import Config


class WishlistPage:
    def __init__(self,driver:WebDriver):
        self.driver:WebDriver = driver
        self.driver.get(Config.BASE_URL+'?route=account/wishlist')
        self.page_title = (By.TAG_NAME,"h2")
        self.wishlist_table = (By.TAG_NAME,"table")
        self.wishlist_table_head = (By.XPATH,"//thead//td")
        self.wishlist_table_elements = (By.XPATH,"//table/tbody/tr")
        self.add_to_cart_btn = (By.XPATH,"//button[@data-original-title='Add to Cart']")
        self.remove_btn = (By.XPATH,"//a[@data-original-title='Remove']")
        self.continue_btn = (By.XPATH,"//a[contains(text(),'Continue')]")
        self.product_link = (By.XPATH,"//a[contains(@href,'route=product/product')]")
    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()

    def click_remove(self):
        self.driver.find_element(*self.remove_btn).click()

    def click_continue(self):
        self.driver.find_element(*self.continue_btn).click()




