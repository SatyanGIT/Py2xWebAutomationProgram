# Selenium 4
import time
import pytest
import allure
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


@pytest.mark.smoke
@allure.title("Verify that Login is working in iDrive360.com website")
@allure.description("TC#1 - Simple Login check on idrive360.com Website.")
def test_iDrive360login():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/")
    #<a href="https://www.idrive360.com/enterprise/login" class="signup">Sign In</a>
    sign_in_btn = driver.find_element(By.LINK_TEXT,"Sign In")
    sign_in_btn.click()
    allure.attach(driver.get_screenshot_as_png(), name="signin_screenshot", attachment_type=AttachmentType.PNG)
    print(driver.current_url)
    assert driver.current_url == "https://www.idrive360.com/enterprise/login", "Assertion Fail Message #1 Error Matching the URLs"

    username = driver.find_element(By.XPATH,"//input[@name='username']")
    username.send_keys("augtest_040823@idrive.com")

    password = driver.find_element(By.XPATH,"//*[@id='password']")
    password.send_keys("123456")

    submit_btn = driver.find_element(By.XPATH, "//*[@id='frm-btn']")
    submit_btn.click()

    allure.attach(driver.get_screenshot_as_png(), name="My Account_screenshot", attachment_type=AttachmentType.PNG)

    #assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true", "Assertion Fail Message #2 Error wrong URL (Upgrade Account)"

    time.sleep(10)
    driver.quit()

    # //*[@id='frm-btn']

    #<button _ngcontent-rwq-c4=""
    # class="id-btn id-info-btn-frm"
    # id="frm-btn"
    # type="submit">Sign in</button>

    # <input _ngcontent-uyn-c4=""
    # class="id-form-ctrl ng-pristine ng-valid ng-touched"
    # id="password"
    # name="password"
    # tabindex="0"
    # type="password">

    # //*[@id="password"]



    #<
    # input _ngcontent-uyn-c4=""
    # autofocus=""
    # class="id-form-ctrl ng-pristine ng-valid ng-touched"
    # id="username"
    # name="username"
    # type="email">








    # make_appointment_btn = driver.find_element(By.XPATH,"//input[@name='username']")
    # make_appointment_btn.send_keys("admin")
    #
    # allure.attach(driver.get_screenshot_as_png(), name="login_screenshot", attachment_type=AttachmentType.PNG)


