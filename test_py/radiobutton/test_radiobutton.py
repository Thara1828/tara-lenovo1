from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_radio_button():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://demoqa.com/radio-button")

    wait = WebDriverWait(driver, 10)

    impressive = wait.until(
        EC.presence_of_element_located((By.XPATH, "//label[@for='impressiveRadio']"))
    )

    # Scroll into view
    driver.execute_script("arguments[0].scrollIntoView(true);", impressive)
    time.sleep(1)

    # Click using JavaScript (avoids interception)
    driver.execute_script("arguments[0].click();", impressive)

    # Assertion
    result = driver.find_element(By.CLASS_NAME, "text-success").text
    assert result == "Impressive"

    driver.quit()
