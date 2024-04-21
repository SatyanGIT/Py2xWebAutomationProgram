# Selenium 4
from selenium import webdriver
import time


def test_open_vwologin():
    driver = webdriver.Chrome()       #open the session - POST Request
    driver.get("https://app.vwo.com")  # GET Request to URL Param
    time.sleep(5)