from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_checkbox():

    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    driver.get("https://demoqa.com/checkbox")

    # Scroll
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Expand Home
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@title='Expand all']")
    )).click()

    # Click Home checkbox (LABEL click)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//label[@for='tree-node-home']")
    )).click()

    time.sleep(2)
    driver.quit()
