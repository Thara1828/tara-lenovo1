from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
time.sleep(2)

# Fetch all product names
products = driver.find_elements(By.CLASS_NAME,"inventory_item_name")

for p in products:
    print(p.text)

print("total products:",len(products))

driver.quit()