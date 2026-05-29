from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
time.sleep(2)

# Add two products
driver.find_elements(By.CLASS_NAME,"btn_inventory")[0].click()
driver.find_elements(By.CLASS_NAME,"btn_inventory")[1].click()

# Navigate to cart
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
time.sleep(2)

# Screenshot
driver.save_screenshot("cart_page.png")

driver.quit()
