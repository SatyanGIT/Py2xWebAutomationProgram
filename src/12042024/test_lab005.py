# Selenium 4
from selenium import webdriver
import time
import pytest
import logging
#@pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome()       #open the session - POST Request
    driver.get("https://app.vwo.com")  # GET Request to URL Param
    print(driver.title)
    #LOGGER.info(driver.title)
    assert driver.title == "Login - VWO"
