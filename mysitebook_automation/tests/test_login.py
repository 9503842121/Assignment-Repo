
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.config import BASE_URL, LOGIN_URL, MOBILE_NUMBER, PASSWORD
from pages.login_page import LoginPage
from pages.project_page import ProjectPage


logging.basicConfig(level=logging.INFO)

@pytest.fixture
def driver():
    # Ensure ChromeDriver is correctly initialized
    driver = webdriver.Chrome()  # Ensure that ChromeDriver path is set if needed
    driver.maximize_window()
    yield driver
    driver.quit()

def select_project_card(driver, project_name):

    try:

        project_card = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{project_name}')]"))
        )
        project_card.click()
        logging.info(f"Successfully selected project card: {project_name}")
    except TimeoutException:
        logging.error(f"Timeout: Project card '{project_name}' not found or not clickable.")
        raise

def test_login_and_project_details(driver):
    driver.get(BASE_URL)
    login_page = LoginPage(driver)


    logging.info("Attempting to close popup if present.")
    try:
        login_page.close_popup()
    except NoSuchElementException:
        logging.info("No popup found to close.")


    login_page.navigate_to_login(LOGIN_URL)
    login_page.login(MOBILE_NUMBER, PASSWORD)
    logging.info("Logged in successfully.")


    project_page = ProjectPage(driver)


    logging.info("Selecting the project card.")
    select_project_card(driver, "Sample bungalow project")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Detailed Estimate')]"))
        )
        project_page.select_quotation("Detailed Estimate")
        logging.info("Selected 'Detailed Estimate' quotation successfully.")
    except TimeoutException:
        logging.error("Timeout while waiting for quotation section to load.")
        raise


    try:
        project_page.verify_details("Tiling", 347.35, "sqft", 30739.03)
        project_page.verify_details("Doors with Frames", 1.00, "No.", 14517.10)
        logging.info("Verified details successfully.")
    except (NoSuchElementException, TimeoutException) as e:
        logging.error(f"Error while verifying details: {e}")
        raise
