import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.search_page import SearchPage
from tests.conftest import login
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging

logger = logging.getLogger(__name__)
def test_add_to_cart_from_search(driver:WebDriver):
    logger.info('Integration testcase to login then go to search page then search a product and add to cart being executed')
    driver = login(driver)
    page = SearchPage(driver)
    page.type_keywords_and_enter('apple')
    page.click_add_to_cart()
    #time.sleep(2)
    try:
        WebDriverWait(driver,2).until(
            EC.url_matches('https://awesomeqa.com/ui/index.php?route=product/product&product_id=42')
        )
    except Exception as e:
        print(f'This was the exception:{e}')
    finally:
        assert driver.current_url =='https://awesomeqa.com/ui/index.php?route=product/product&product_id=42'

