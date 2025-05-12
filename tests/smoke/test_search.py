import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pages.home_page import HomePage


def test_search(driver:WebDriver):
    page = HomePage(driver)
    search_key = 'iphone'
    page.type_search(search_key)
    page.click_search()
    products = page.get_products_title()
    for product in products:
        assert product.lower()==search_key
        print(f'{product.lower()} is searched successfully')

    
