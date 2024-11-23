# Evan Inman

from dateutil.utils import today
from jinja2.runtime import to_string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time

def Test_Add_Book():
    chrome_driver_path = '/usr/local/bin/chromedriver/chromedriver'  # Adjust the path as needed
    service = Service(chrome_driver_path)

    # Initialize the Chrome WebDriver with the service object
    driver = webdriver.Chrome(service=service)

    driver.get("http://localhost:8069/web#action=415&model=library.book&view_type=list&cids=1&menu_id=305")

    # These require the proper login name and password to function
    driver.find_element(By.NAME, "login").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("changeme")
    driver.find_element(By.XPATH, "//button[@type='submit']").submit()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "btn.btn-primary.o_list_button_add").click()
    time.sleep(2)
    driver.find_element(By.ID, "name").send_keys("Test Title")
    driver.find_element(By.ID, "author_ids").send_keys("Test Author")
    driver.find_element(By.ID, "date_release").send_keys(to_string(today()))
    driver.find_element(By.ID, "color").send_keys("2")
    driver.find_element(By.CLASS_NAME, "o_form_button_save.btn.btn-light.py-0").click()

    driver.quit()

def main():
    Test_Add_Book()

if __name__ == "__main__":
    main()
