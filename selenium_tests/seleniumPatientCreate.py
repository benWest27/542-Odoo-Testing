# Benjamin West

from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from testing_selenium import password
load_dotenv()

PASSWORD = os.getenv("PASSWORD")
USERNAME = os.getenv("USERNAME")
WEBDRIVER = os.getenv("WEBDRIVER")

if WEBDRIVER == "firefox":
    driver = webdriver.Firefox()
else:
    driver = webdriver.Chrome()

def update_form_field(driver, field_name, field_value):

    time.sleep(1)
    field = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.NAME,field_name))
    )
    field.clear()
    time.sleep(1)
    field.send_keys(field_value)

driver.get("http://localhost:8069/web#menu_id=285&action=395")

search_bar = driver.find_element(By.NAME, "login")
search_bar.clear()
time.sleep(1)
search_bar.send_keys("benjamin.west.217@gmail.com")
print("Entered email")
time.sleep(1)

search_bar = driver.find_element(By.NAME, "password")
print("Entered Password")
time.sleep(1)
search_bar.send_keys(PASSWORD)
time.sleep(1)
#search_bar.clear()
search_bar.send_keys(Keys.RETURN)
time.sleep(1)

print("Navigated to om_hospital")

#create_button_1 = driver.find_element(By.XPATH,'/html/body//button').click()
create_button = WebDriverWait(driver, 10).until(
     ec.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary.o_list_button_add"))
)
create_button.click()

update_form_field(driver, "name", "John Doe")
update_form_field(driver, "age", "45")

gender_dropdown = Select(driver.find_element(By.XPATH, "//select[@name='gender']"))
gender_dropdown.select_by_value("\"male\"")
# driver.find_element(By.XPATH, "//option[@value='male']").click()
driver.find_element(By.CSS_SELECTOR, "button[title='Save record']").click()

save_button = WebDriverWait(driver, 10).until(
     ec.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary.o_form_button_save"))
)
save_button.click()

print("Test Passed")
driver.close()
