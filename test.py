from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://demoqa.com/checkbox')
wait = WebDriverWait(driver, 10)

way = ('/xpath', "//path")
wait.until(EC.element_to_be_clickable(way)).click()
time.sleep(5)

driver.quit()
