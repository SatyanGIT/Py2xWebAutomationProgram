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
    driver.maximize_window()
    print(driver.page_source)
    print(driver.session_id)
    # Session is created - Unique ID - 16 Digit
    # Session - A fresh copy of browser is created - webdriver.chrome()
    assert driver.title == "Login - VWO"

    driver.close()
    # close will close the current window or tab
    # session ID != null
    driver.quit()
    # close all the wndows or tabs
    # session ID == null(Invalid)
    time.sleep(10)