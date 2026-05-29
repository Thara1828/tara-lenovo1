from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

expected_title="swag Labs"
actual_title=driver.title


if expected_title==actual_title:
    print("title matched")
else:
    print("title not matched")
    print("actual title is",actual_title)

driver.quit()