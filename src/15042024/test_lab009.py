# Selenium 4
from selenium import webdriver
import time
import pytest
import logging
#@pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome()       #open the session - POST Request
    driver.get("https://bing.com/chat")  # GET Request to URL Param
    time.sleep(25) # python interpreter- wait for 25 sec, not for webdriver
    driver.get("https://google.com")
    print(driver.title)
