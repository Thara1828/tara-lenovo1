from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.google.com/")

driver.find_element(By.TAG_NAME,"a").click()
driver.switch_to.window(driver.window_handles[0])

print(driver.title)

time.sleep(4)
driver.quit()