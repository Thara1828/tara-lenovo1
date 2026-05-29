from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")


driver.find_element(By.CSS_SELECTOR, "#userName").send_keys("Thara")
driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("thara@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys("Madurai")
driver.find_element(By.CSS_SELECTOR, "#permanentAddress").send_keys("Tamil Nadu")


driver.find_element(By.CSS_SELECTOR, "#submit").click()
time.sleep(2)


driver.save_screenshot("demoqa_form.png")

driver.quit()
