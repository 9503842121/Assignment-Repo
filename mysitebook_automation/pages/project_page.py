
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProjectPage:
    def __init__(self, driver):
        self.switch_to = None
        self.driver = driver


    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    def select_project_card(driver, project_name="Sample bungalow project"):

        project_card_xpath = f"//div[contains(@class, 'mbc-projects-card')]//span[normalize-space()='{project_name}']"

        try:
            # Wait until the project card is clickable, then click it
            project_card_element = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, project_card_xpath))
            )

            project_card_element.click()
            print(f"Selected project card: {project_name}")
        except Exception as e:
            print(f"Could not select the project card: {project_name}. Error: {e}")
            driver.switch_to.frame("frame_id_or_name")  # Replace with the actual frame id or name

            element = driver.find_element(By.XPATH, project_card_xpath)
            driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()

    def select_quotation(self, quotation_name):
        """Selects the specified quotation by name."""
        quotation_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[@class='list-group-item list-group-item-action active' and text()='{quotation_name}']"))
        )
        quotation_element.click()
        print(f"Selected quotation: {quotation_name}")

    def verify_details(self, section, expected_quantity, expected_unit, expected_cost):

        quantity_element = self.driver.find_element(By.XPATH, f"//div[@data-section='{section}']//td[@id='quantity']")
        unit_element = self.driver.find_element(By.XPATH, f"//div[@data-section='{section}']//td[@id='unit']")
        cost_element = self.driver.find_element(By.XPATH, f"//div[@data-section='{section}']//td[@id='cost']")

        assert float(quantity_element.text) == expected_quantity, f"Quantity mismatch for {section}"
        assert unit_element.text.strip() == expected_unit, f"Unit mismatch for {section}"
        assert float(cost_element.text.replace(',', '')) == expected_cost, f"Cost mismatch for {section}"

    def execute_script(self, param, element):
        pass

    def find_element(self, XPATH, project_card_xpath):
        pass


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def select_project_card(driver, project_name="Sample bungalow project"):
    project_card_xpath = f"//div[contains(@class, 'mbc-projects-card')]//span[normalize-space()='{project_name}']"

    try:

        project_card_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, project_card_xpath))
        )


        driver.execute_script("arguments[0].scrollIntoView();", project_card_element)

        project_card_element.click()
        print(f"Selected project card: {project_name}")
    except TimeoutException as e:
        print(f"TimeoutException: Could not select the project card '{project_name}'. Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
