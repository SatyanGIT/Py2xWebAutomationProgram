# Selenium 4
from selenium import webdriver


def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    # Python interpreter -> optimise if there is not command. I will stop the execution