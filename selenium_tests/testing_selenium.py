#Israel Garcia Figueroa
#cpsc 542 -
# selenium test cases, log in testing,
# need one more s
from contextlib import nullcontext

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.input_ import dispatch_key_event
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

# Provide the absolute or relative path to your chromedriver
chrome_driver_path = './drivers/chromedriver'  # Adjust the path as needed

# Set up the service object
service = Service(chrome_driver_path)

# Initialize the Chrome WebDriver with the service object
#driver = webdriver.Chrome(service=service)
driver = webdriver.Firefox()

username = "benjamin.west.217@gmail.com"
password = "5678tyui%^&*TYUI"

#===============Log In test
# Open a webpage to test


# Print the page title
def update_form_field(driver, field_name, field_value):
	search_bar = driver.find_element(By.NAME, field_name)
	search_bar.clear()
	time.sleep(1)
	search_bar.send_keys(field_value)

def TestLogin():
    service = Service(chrome_driver_path)

    # Initialize the Chrome WebDriver with the service object
    # driver = webdriver.Chrome(service=service)
    driver = webdriver.Firefox()

    driver.get("http://localhost:8069/web/login")
    update_form_field(driver, "login", username)
    #update to proper field values
    update_form_field(driver, field_name="password", field_value=password)
    driver.find_element(By.NAME, "login").send_keys(Keys.RETURN)
    try:
        alert_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "p.alert.alert-danger"))
        )
        print("this is the alert text found with alert-danger class: " , alert_element.text)
        assert alert_element.text == "Wrong login/password", "FAILED"
    except:
        print("Passed: valid Log in test.")
    finally:
        driver.quit()
#testing negative odometer on odo
def Test_Odo():
    service = Service(chrome_driver_path)

    # Initialize the Chrome WebDriver with the service object
    #driver = webdriver.Chrome(service=service)
    driver = webdriver.Firefox()

    driver.get("http://localhost:8069/web#cids=1&menu_id=97&action=128&model=fleet.vehicle&view_type=kanban")

    update_form_field(driver, "login", username)
    #update to proper field values
    update_form_field(driver, field_name="password", field_value=password)
    driver.find_element(By.NAME, "login").send_keys(Keys.RETURN)

    #adding new car
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="Create record"]'))
    )
    button.click()
    time.sleep(2)
    input_field = driver.find_element(By.CSS_SELECTOR, 'input[id^="o_field_input_"]')
    input_field.clear()  # Optional: clear the field if necessary
    time.sleep(2)
    input_field.send_keys("Audi/A3")
    input_field.send_keys(Keys.TAB)

    bool_check = nullcontext
    try:
        modal_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "modal-body"))
            )
        if "Create Audi/A3 as a new Model?" in modal_text.text:
            bool_check = True
        else:
            bool_check = False
        assert bool_check == False, print("Failed Test Case, Make and model already exist")
    except:
        print("This will create the Same Make making it redundant")
    finally:
        driver.quit()
def main():
    TestLogin()
    Test_Odo()

if __name__ == "__main__":
    main()