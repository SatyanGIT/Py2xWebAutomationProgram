# Selenium 4
import time
import pytest
import allure
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


@pytest.mark.smoke
@allure.title("Verify that Login is working in Cura website")
@allure.description("TC#1 - Simple Login check on cura katalon Website.")
def test_katalonlogin_tc():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    #<
    # input type="text"
    # class="form-control"
    # id="txt-username"
    # name="username"
    # placeholder="Username"
    # value="" autocomplete="off"
    # >

    # Xpath
    # // input[@id='txt-username']
    # // input[@name='username']
    # // input[@class='form-control'] - Not Recommended
    # // input[@type='"text"] - Not Recommended
