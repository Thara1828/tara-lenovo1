from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Enter username using NAME
driver.find_element(By.NAME,"user-name").send_keys("standard_user")

# Enter password using ID
driver.find_element(By.ID,"password").send_keys("secret_sauce")

# Click login
driver.find_element(By.ID,"login-button").click()
time.sleep(2)

# Print current URL
print("Current URL:", driver.current_url)

driver.quit()
