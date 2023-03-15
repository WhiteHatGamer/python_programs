from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("https://google.co.in")

elem= driver.find_element(By.NAME, "q")
print(elem)
elem.clear()
elem.send_keys("Python using selenium")
elem.send_keys(Keys.RETURN)
time.sleep(5)

driver.close()
