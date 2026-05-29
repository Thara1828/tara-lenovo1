from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_text_box_form():

    driver = webdriver.Chrome()
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    driver.get("https://demoqa.com/text-box")

    # Wait & fill Full Name
    wait.until(EC.visibility_of_element_located((By.ID, "userName"))).send_keys("Vignaya Sathyskanth")

    driver.find_element(By.ID, "userEmail").send_keys("test@gmail.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Chennai")
    driver.find_element(By.ID, "permanentAddress").send_keys("Tamil Nadu")

    # Scroll (IMPORTANT for DemoQA)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    driver.find_element(By.ID, "submit").click()

    time.sleep(2)
    driver.quit()
