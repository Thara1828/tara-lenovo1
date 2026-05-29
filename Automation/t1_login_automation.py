from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

# Valid Login
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

if "Logged In Successfully" in driver.page_source:
    print("PASS - Valid login successful")
else:
    driver.save_screenshot("fail_valid_login.png")
    print("FAIL - Valid login failed")

# Invalid Login
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

error = driver.find_element(By.ID, "error")
if error.is_displayed():
    print("PASS - Error message shown:", error.text)
else:
    driver.save_screenshot("fail_invalid_login.png")
    print("FAIL - Error message not shown")

time.sleep(2)
driver.quit()