
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def close_popup(self):

        try:
            close_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//img[@src='https://mysitebook.io/wp-content/themes/mysitebook/assets/images/knowledge/close.svg']"))
            )
            close_button.click()
            print("Popup closed successfully.")
        except:
            print("Popup not found or could not be closed.")

    def navigate_to_login(self, url):
        self.driver.get(url)

    def login(self, mobile_number, password):

        mobile_input = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.ID, "mobileNumber"))
        )
        mobile_input.clear()
        mobile_input.send_keys(mobile_number)

        continue_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue']"))
        )
        continue_button.click()


        password_input = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password_input.send_keys(password)

        login_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))
        )
        login_button.click()
