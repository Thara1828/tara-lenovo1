from selenium import webdriver#webdriver used for opening the browser
from selenium.webdriver.common.by import By #By-locating element(path)
from selenium.webdriver.support.ui import WebDriverWait #webdriver-wait till loading element
from selenium.webdriver.support import expected_conditions as EC #EC-visible,clickable
import time

def test_practice_form():

    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    driver.get("https://demoqa.com/automation-practice-form")

    wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys("Thara")
    driver.find_element(By.ID, "lastName").send_keys("G")
    driver.find_element(By.ID, "userEmail").send_keys("thara@test.com")

    # Gender FIX
    female = wait.until(
        EC.presence_of_element_located((By.XPATH, "//label[@for='gender-radio-2']"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", female)
    driver.execute_script("arguments[0].click();", female)

    # Mobile
    driver.find_element(By.ID, "userNumber").send_keys("9876543210")

    driver.quit()
