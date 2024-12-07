from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = 'C:\Chromedriver\chromedriver-win64\chromedriver.exe'

def login_to_odoo(driver, username, password):
    driver.get("http://localhost:8069/web/login")
    update_form_field(driver, "login",  "Admin")
    update_form_field(driver, "password", "Admin")
    driver.find_element(By.NAME, "login").send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".o_user_menu"))
    )

def update_form_field(driver, field_name, field_value):
    field = driver.find_element(By.NAME, field_name)
    field.clear()
    time.sleep(1)
    field.send_keys(field_value)

def TestAddDoctor():
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)

    try:
        #Log in to Odoo
        login_to_odoo(driver, "Admin", "Admin")
        print("Login successful.")

        # Navigate to the page
        driver.get("http://localhost:8069/web#action=475&model=hospital.doctor&view_type=kanban&cids=1&menu_id=346")
        print("Navigated to the page.")

        new_button_kanban = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.o-kanban-button-new"))
        )
        new_button_kanban.click()
        print("Create doctor profile.")

        doctor_name_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "doctor_name"))
        )
        doctor_name_field.clear()
        doctor_name_field.send_keys("Dr. John Doe")
        print("Entered Doctor Name.")

        #Fill the Age field
        age_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "age"))
        )
        age_field.clear()
        age_field.send_keys("45")
        print("Entered Age.")

        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button > i.fa.fa-cloud-upload.fa-fw"))
        )
        save_button.click()
        print("Clicked the 'Save' button.")

        #Confirm the record is saved
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Dr. John Doe')]"))
        )
        print("Record saved successfully, test passed !")

    except Exception as e:
        print(f"General failure: {e}")
        driver.save_screenshot("general_error.png")
        raise

    finally:
        input("Press Enter to close the browser...")
        driver.quit()


if __name__ == "__main__":
    TestAddDoctor()
