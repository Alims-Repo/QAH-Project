import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pages.search_page import SearchPage
from pages.login_page import LoginPage
from utils.csv_reader import read_csv

# this test_login will be required later when we have to first login and then perform action
@pytest.mark.skip
def test_login(driver:WebDriver):
    page = LoginPage(driver)
    page.type_email('dnewiss0@usatoday.com')
    page.type_password('bR4Dv)>>GS6rqayT')
    page.click_login()
    assert driver.current_url.endswith('?route=account/account')
    print(f'user is logged in successfully')
    return driver


products_data = read_csv('test_data/Products_data.csv')

@pytest.mark.skip
@pytest.mark.parametrize("data", products_data)
def test_search_one_keyword(driver:WebDriver,data):
    #driver:WebDriver = test_login(driver)
    value = data[0]
    page = SearchPage(driver)
    print(f'Performing search operation on {value}')
    page.type_keywords_and_enter(value)
    assert page.product_name_check(value)==True
    print('product search working correctly')
