# Evan Inman
import os
from dateutil.utils import today
from jinja2.runtime import to_string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

import time


PASSWORD = "PASSWORD"
USERNAME = "USERNAME"

def Test_Add_Book():
    chrome_driver_path = '/usr/local/bin/chromedriver/chromedriver'  # Adjust the path as needed
    service = Service(chrome_driver_path)

    # Initialize the Chrome WebDriver with the service object
    driver = webdriver.Firefox()

    driver.get("http://localhost:8069/web#action=415&model=library.book&view_type=list&cids=1&menu_id=305")

    # These require the proper login name and password to function
    driver.find_element(By.NAME, "login").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").submit()
    time.sleep(1)

    create_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary.o_list_button_add"))
    )
    create_button.click()
    #Screate_button = WebDriverWait(driver, 10).until(
    #driver.find_element(By.CLASS_NAME, "btn.btn-primary.o_list_button_add").click()

    #create_button.click()
    #
    time.sleep(2)
    driver.find_element(By.NAME, "name").send_keys("Test Title")
    driver.find_element(By.NAME, "address").send_keys("Test address")
    driver.find_element(By.NAME, "description").send_keys(to_string(today()))
    #driver.find_element(By.ID, "color").send_keys("2")
    save_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary.o_form_button_save"))
    )
    save_button.click()
   # driver.find_element(By.CLASS_NAME, "o_form_button_save.btn.btn-light.py-0").click()
    print("Test Successful")
    driver.quit()

def main():
    Test_Add_Book()

if __name__ == "__main__":
    main()
