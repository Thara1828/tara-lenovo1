from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

#login
driver.find_element(By.ID,"user-name").send_keys("error_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

time.sleep(4)

#adding product to cart
driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
time.sleep(3)

# Open cart page
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
time.sleep(2)

driver.quit()