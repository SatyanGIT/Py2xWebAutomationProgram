# Selenium 4
import time
import pytest
import allure
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


@pytest.mark.smoke
@allure.title("Verify that Login is working in app.vwo.com website")
@allure.description("TC#1 - Simple Login check on vwo.com Website.")
def test_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")

    #<input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi">

    # Xpath
    # // input[@id='login-username']
    # // input[@name='username']
    # // input[@class='text-input W(100%)'] - Not Recommended
    # // input[@type='"email"] - Not Recommended
    # // input[@data-qa="hocewoqisi"] - Custom A

    make_appointment_btn = driver.find_element(By.XPATH,"//input[@name='username']")
    make_appointment_btn.send_keys("admin")

    allure.attach(driver.get_screenshot_as_png(), name="login_screenshot", attachment_type=AttachmentType.PNG)

    driver.quit()
