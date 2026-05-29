from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")
time.sleep(2)

# Switch to iframe
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, "demo-frame"))
)

draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")

print("Before drop:", droppable.text)

ActionChains(driver).drag_and_drop(draggable, droppable).perform()
time.sleep(2)

print("After drop:", droppable.text)

if "Dropped" in droppable.text:
    print("PASS - Drag and drop successful")
else:
    print("FAIL - Drag and drop not working")

driver.quit()