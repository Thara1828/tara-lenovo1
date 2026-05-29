from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/products")
time.sleep(2)

# ── Search for Tops ──────────────────────────────────────────
driver.find_element(By.ID, "search_product").send_keys("Tops")
driver.find_element(By.ID, "submit_search").click()
time.sleep(2)

products = driver.find_elements(By.CLASS_NAME, "productinfo")
print("Search Results for 'Tops':", len(products), "products found")

for p in products:
    name = p.find_element(By.TAG_NAME, "p").text
    print(" -", name)

# ── Category Filter - Women > Dress ──────────────────────────
driver.get("https://automationexercise.com/products")
time.sleep(2)

# Expand Women panel
women = driver.find_element(By.XPATH, "//a[@href='#Women']")
driver.execute_script("arguments[0].click()", women)
time.sleep(1)

# Click Dress
dress = driver.find_element(By.XPATH, "//div[@id='Women']//a[contains(text(),'Dress')]")
driver.execute_script("arguments[0].click()", dress)
time.sleep(2)

filtered = driver.find_elements(By.CLASS_NAME, "productinfo")
print("\nCategory Filter - Women > Dress:", len(filtered), "products found")

for p in filtered:
    name = p.find_element(By.TAG_NAME, "p").text
    print(" -", name)

# ── Category Filter - Men > Tshirts ──────────────────────────
driver.get("https://automationexercise.com/products")
time.sleep(2)

# Expand Men panel
men = driver.find_element(By.XPATH, "//a[@href='#Men']")
driver.execute_script("arguments[0].click()", men)
time.sleep(1)

# Click Tshirts
tshirts = driver.find_element(By.XPATH, "//div[@id='Men']//a[contains(text(),'Tshirts')]")
driver.execute_script("arguments[0].click()", tshirts)
time.sleep(2)

filtered2 = driver.find_elements(By.CLASS_NAME, "productinfo")
print("\nCategory Filter - Men > Tshirts:", len(filtered2), "products found")

for p in filtered2:
    name = p.find_element(By.TAG_NAME, "p").text
    print(" -", name)

driver.quit()