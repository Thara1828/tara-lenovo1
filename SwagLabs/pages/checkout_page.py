from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_details(self, first, last, zip_code):
        self.wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    def finish_order(self):
        finish_btn = self.wait.until(EC.presence_of_element_located((By.ID, "finish")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", finish_btn)
        self.driver.execute_script("arguments[0].click();", finish_btn)

    def get_success_text(self):
        success = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        return success.text