# Selenium 4
from selenium import webdriver
import time
import pytest
import logging
from selenium.webdriver.common.by import By


# @pytest.mark.smoke
def test_vwologin_negative_tc():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")

    # id -> name -> className -> LinkText, Partial -> css Selector -> Xpath
    # <input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >

    email_element = driver.find_element(By.NAME, "username")
    email_element.send_keys("admin")

    # <input
    # type="password"
    # class="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe">

    password_element = driver.find_element(By.ID, "login-password")
    password_element.send_keys("admin")

    # <button type="submit"
    # id="js-login-btn"
    # class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica">

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()

    time.sleep(5)

    # <div class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">Your email,
    # password,
    # IP address or location did not match</div>

    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"
    driver.quit()
