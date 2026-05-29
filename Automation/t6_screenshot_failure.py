from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

os.makedirs("screenshots", exist_ok=True)

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

def take_screenshot(name):
    path = f"screenshots/{name}.png"
    driver.save_screenshot(path)
    print(f"Screenshot saved → {path}")


print("\n[TEST 1] Intentional fail — wrong password")
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("wrongpassword")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

if "Logged In Successfully" in driver.page_source:
    print("PASS - Logged in")
else:
    take_screenshot("fail_wrong_password")
    print("FAIL - Wrong password — screenshot saved")


print("\n[TEST 2] Intentional fail — wrong username")
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(1)
driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

if "Logged In Successfully" in driver.page_source:
    print("PASS - Logged in")
else:
    take_screenshot("fail_wrong_username")
    print("FAIL - Wrong username — screenshot saved")


print("\n[TEST 3] Intentional fail — empty fields")
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(1)
driver.find_element(By.ID, "submit").click()
time.sleep(2)

if "Logged In Successfully" in driver.page_source:
    print("PASS - Logged in")
else:
    take_screenshot("fail_empty_fields")
    print("FAIL - Empty fields — screenshot saved")


print("\n[TEST 4] Valid login — should pass")
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(1)
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

if "Logged In Successfully" in driver.page_source:
    print("PASS - Valid login successful")
else:
    take_screenshot("fail_valid_login_unexpected")
    print("FAIL - Unexpected failure — screenshot saved")

print("\n── Test Report ──────────────────────────────")
screenshots = os.listdir("screenshots")
print(f"Total screenshots captured : {len(screenshots)}")
for s in screenshots:
    print(f"  → screenshots/{s}")

driver.quit()