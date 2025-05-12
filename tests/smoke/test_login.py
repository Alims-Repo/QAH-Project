import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pages.login_page import LoginPage

from utils.csv_reader import read_csv
login_data = read_csv('test_data/MOCK_DATA.txt')



@pytest.mark.parametrize("data",login_data)
def test_login(driver:WebDriver,data):
    page = LoginPage(driver)
    page.type_email(data[2])
    page.type_password(data[4])
    page.click_login()
    assert driver.current_url.endswith('?route=account/account')
    print(f'email:{data[2]} is logged in successfully')