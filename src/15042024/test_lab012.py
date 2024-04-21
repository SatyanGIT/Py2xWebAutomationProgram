# Selenium 4
from selenium import webdriver
import time
import pytest
import logging
from selenium.webdriver.common.by import By
#@pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # < a
    # id = "btn-make-appointment"
    # href = "./profile.php#login"
    # class ="btn btn-dark btn-lg"
    # >
    # Make Appointment
    # < / a >

    # Find the  element anchor tag - button
    # Click on it

    # Easy 1. id, classname, name, tagname, linktext, partial linktext
    #2. css Selector , Xpath (Sure short way to find the elements in HTML)

    element = driver.find_element(By.ID,value = "btn-make-appointment")
    element.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(25)
    driver.quit()




  