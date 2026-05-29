from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")


driver.find_element(By.ID, "login-button").click()
time.sleep(3)


driver.save_screenshot("valid_login.png")

# Close browser
driver.quit()
