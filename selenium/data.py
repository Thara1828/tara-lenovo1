from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

# Wait and click Sauce Labs Onesie
WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//div[text()='Sauce Labs Onesie']"))
).click()

time.sleep(2)
driver.quit()
