from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

time.sleep(2)

username=driver.find_element(By.ID,"user-name").get_attribute("placeholder")
print(username)
password=driver.find_element(By.ID,"password").get_attribute("placeholder")
print(password)
button=driver.find_element(By.ID,"login-button")

time.sleep(3)
driver.quit()