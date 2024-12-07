
from dotenv import load_dotenv
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
USERNAME = os.getenv("USERNAME")
WEBDRIVER = os.getenv("WEBDRIVER")

chrome_driver_path = './drivers/chromedriver'

def login_to_odoo(driver, username, password):
    driver.get("http://localhost:8069/web/login")
    update_form_field(driver, "login", username)
    update_form_field(driver, "password", password)
    driver.find_element(By.NAME, "login").send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".o_user_menu"))
    )

def update_form_field(driver, field_name, field_value):

    field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME,field_name))
    )
    field.clear()
    time.sleep(1)
    field.send_keys(field_value)

def TestAddDoctor():
    service = Service(chrome_driver_path)
    driver = webdriver.Firefox()

    try:
        login_to_odoo(driver,"benjamin.west.217@gmail.com",PASSWORD)

        driver.get("http://localhost:8069/web#action=om_hospital.action_hospital_doctor")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Create record']"))
        )

        driver.find_element(By.CSS_SELECTOR, "button[title='Create record']").click()
        update_form_field(driver, "doctor_name", "Dr. John Doe")
        update_form_field(driver, "age", "45")
        gender_dropdown = Select(driver.find_element(By.XPATH, "//select[@name='gender']"))
        gender_dropdown.select_by_value("\"male\"")
        #driver.find_element(By.XPATH, "//option[@value='male']").click()
        driver.find_element(By.CSS_SELECTOR, "button[title='Save record']").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Dr. John Doe')]"))
        )
        print("Passed: Doctor record created successfully.")

    except Exception as e:
        driver.save_screenshot("error_screenshot.png")
        print(f"Failed: Could not create doctor record. Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    TestAddDoctor()