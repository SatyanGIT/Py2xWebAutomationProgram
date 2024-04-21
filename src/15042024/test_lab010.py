# Selenium 4
from selenium import webdriver
import time
import pytest
import logging
#@pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome()       #open the session - POST Request
    # driver.navigate()
    # navigate commands are not present in python
    driver.get("https://bing.com/chat")
    driver.back()
    driver.get("https://google.com")
    print(driver.title)
    driver.forward()
    print(driver.title)
    driver.back()
    print(driver.title)
    driver.refresh()
    time.sleep(5)
    driver.quit()




  