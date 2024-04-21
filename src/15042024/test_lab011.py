# Selenium 4
from selenium import webdriver
import time
import pytest
import logging
#@pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")

    # we should interact with the html elements
    # Locators - Xpath, Css selectors

    driver.quit()




  