import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from utils.driver_factory import get_driver
from utils.config import Config
from pages.login_page import LoginPage


@pytest.fixture(scope='function')
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def login(driver:WebDriver):
    page = LoginPage(driver)
    page.type_email('dnewiss0@usatoday.com')
    page.type_password('bR4Dv)>>GS6rqayT')
    page.click_login()
    return driver

import pytest

@pytest.fixture
def screenshot_path(request):
    return request.config.getoption("--screenshot_path")


def pytest_addoption(parser):
    parser.addoption(
        "--screenshot_path",
        action="store",
        default=None,
        help="Path to save screenshots"
    )