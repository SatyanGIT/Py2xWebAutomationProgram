# Selenium 4
from selenium import webdriver
import time
import pytest
import logging
from selenium.webdriver.common.by import By


# @pytest.mark.smoke
def test_katalonlogin_tc():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    #driver.find_element(By.ID,"btn-make-appointment").click()

    # By. Link Text - Full Match or Exact match with the text
    # a tag -> anchor tag

    # <a
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a>

    # make_appointment_btn = driver.find_element(By.LINK_TEXT,"Make Appointment")
    # make_appointment_btn.click()
    #
    # time.sleep(20)

  # Partial Text
  # a anchor
  # partial match
  # PARTIAL_LINK_TEXT
  # Make Appointment
  # Appointment
  # Make
  # App
  # Ment
  # Contains - Keyword
  # Find the first unique element

    # make_appointment_btn = driver.find_element(By.PARTIAL_LINK_TEXT,"Appointment")
    # make_appointment_btn.click()
    #
    # time.sleep(20)
    # driver.quit()
    #
    # By Tagname

    list_of_a_tags = driver.find_elements(By.TAG_NAME,"a")
    make_appointment_btn = list_of_a_tags[5]
    make_appointment_btn.click()

    time.sleep(20)
    driver.quit()
