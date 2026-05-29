from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

links = driver.find_elements(By.TAG_NAME, 'a')
para = driver.find_elements(By.TAG_NAME, 'p')
heading = driver.find_elements(By.TAG_NAME, 'h1')
pre = driver.find_elements(By.TAG_NAME, 'pre')
ol = driver.find_elements(By.TAG_NAME, 'ol')
ul = driver.find_elements(By.TAG_NAME, 'ul')

print(len(links))
print(len(para))
print(len(heading))
print(len(pre))
print(len(ol))
print(len(ul))
