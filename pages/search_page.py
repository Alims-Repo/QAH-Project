import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.config import Config
from selenium.webdriver import Chrome
import logging

class SearchPage:
    logger = logging.getLogger(__name__)
    def __init__(self,driver:WebDriver):
        self.logger.info('Search object initialized')
        self.driver:WebDriver = driver
        self.driver.get(Config.SEARCH_URL)
        self.page_title = (By.TAG_NAME,'h1')
        self.keywords_txt = (By.XPATH,"//input[contains(@placeholder,'Keywords')]")
        self.categories_select = (By.XPATH,"//select[@name='category_id']")
        self.subcategories_check = (By.XPATH,"//input[@name='sub_category']")
        self.description_check = (By.XPATH,"//input[@id='description']")
        self.search_btn = (By.XPATH,"//input[@value='Search']")
        self.product_cards = (By.XPATH,"//div[@class='product-thumb']")
        self.product_names_label = (By.XPATH,"//div[@class='caption']/h4/a")
        self.add_to_cart_btn = (By.XPATH,"//div[@class='button-group']/button[1]/i")

    def check_search_page(self)->bool:
        self.logger.info('search page check is being executed')
        # validates if the page is search page
        if self.driver.find_element(*self.page_title).is_displayed():
            return True

        else:
            return False


    def type_keywords_and_enter(self,value:str) -> None:
        self.logger.info('typing keywords to search field and clicking enter button test')
        # types keyword and clicks enter
        keyword_element = self.driver.find_element(*self.keywords_txt)
        keyword_element.send_keys(*value)
        keyword_element.send_keys(Keys.ENTER)

    def click_add_to_cart(self):
        self.logger.info('Add to cart button click function being executed')
        self.driver.find_element(*self.add_to_cart_btn).click()


    def product_name_check(self,value:str):
        # only incomment next line when performing unit testing
        #self.type_keywords_and_enter(value)
        self.logger.info('products search from cards being executed')
        cards = self.driver.find_elements(*self.product_cards)
        for card in cards:
            if value.lower() in card.find_element(*self.product_names_label).text.lower():
                return True
        return False


# for unit testing
# driver = Chrome()
# p1 = SearchPage(driver)
# driver.implicitly_wait(10)
# print(p1.product_name_check('Lenovo'))
#

