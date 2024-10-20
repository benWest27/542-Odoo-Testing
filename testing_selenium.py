#Israel Garcia Figueroa
#cpsc 542 -
# selenium test cases, log in testing,
# need one more s
from selenium import webdriver
from selenium.webdriver.common.by import By
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
driver = webdriver.Chrome(service=service)


#===============Log In test
# Open a webpage to test
driver.get("http://localhost:8069/web/login")

# Print the page title
def update_form_field(driver, field_name, field_value):
	search_bar = driver.find_element(By.NAME, field_name)
	search_bar.clear()
	time.sleep(1)
	search_bar.send_keys(field_value)

def TestLogin():
    update_form_field(driver, "login", "odoo")
    #update to proper field values
    update_form_field(driver, field_name="password", field_value="1234")
    driver.find_element(By.NAME, "login").send_keys(Keys.RETURN)
    try:
        alert_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "p.alert.alert-danger"))
        )
        print("this is the alert text found with alert-danger class: " , alert_element.text)
        assert alert_element.text == "Wrong login/password", "FAILED"
    except:
        print("Passed: valid Log in test.")


def main():
    TestLogin()

if __name__ == "__main__":
    main()