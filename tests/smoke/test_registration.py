import pytest
from pages.registration_page import RegistrationPage
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver
from utils.csv_reader import read_csv

registration_data = read_csv('test_data/MOCK_DATA.txt')


@pytest.mark.parametrize("data",registration_data)
def test_registration(driver:WebDriver,data):
    page = RegistrationPage(driver)
    page.type_firstname(data[0])
    page.type_lastname(data[1])
    page.type_email(data[2])
    page.type_telephone(data[3])
    page.type_password(data[4])
    page.type_confirm_password(data[4])
    page.click_subscribe(data[5])
    page.click_agree()
    page.click_continue()
    # checks for user warning regarding user already exist
    if page.check_warning_exist():
        pass
    # checks if url ends with success pattern
    else:
        assert driver.current_url.endswith('account/success')
        print(f'email:{data[2]} is registered successfully')

