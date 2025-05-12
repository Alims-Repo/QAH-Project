from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

def get_data_from_element(driver:WebDriver,url:str,web_element:tuple)->list:
    driver.get(url)
    elements = driver.find_elements(*web_element)
    data = []
    for element in elements:
        data.append(element.text)
    return data