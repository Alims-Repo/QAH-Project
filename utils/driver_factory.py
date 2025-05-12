from selenium import webdriver
from utils.config import Config
from selenium.webdriver.remote.webdriver import WebDriver

def get_driver()->WebDriver:
    if Config.BROWSER=='chrome':
        return webdriver.Chrome()
    if Config.BROWSER=='firefox':
        return webdriver.Firefox()
    else:
        return f"{Config.BROWSER} is not supported"
