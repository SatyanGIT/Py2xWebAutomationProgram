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

    make_appointment_btn = driver.find_element(By.LINK_TEXT, "Make Appointment")
    make_appointment_btn.click()

    allure.attach(driver.get_screenshot_as_png(), name="login_screenshot", attachment_type=AttachmentType.PNG)

    print(driver.current_url)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Assertion Fail Message #1 Error Matching the URLs"

    username = driver.find_element(By.NAME, "username")
    username.send_keys("John Doe")

    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")

    Login_btn = driver.find_element(By.ID, "btn-login")
    Login_btn.click()

    allure.attach(driver.get_screenshot_as_png(), name="appointment_screenshot", attachment_type=AttachmentType.PNG)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Assertion Fail Message #2 Error wrong URL (appointment)"

    # //a[@id='btn-make-appointment'] -> 1 unique element

    driver.quit()
