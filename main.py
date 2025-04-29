import os
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}/downloads"
}

chrome_options.add_experimental_option('prefs', prefs)
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--incognito')
# chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--disable-cache')
chrome_options.page_load_strategy = 'normal'


driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)
driver.get(os.getenv('ADP'))

login_form = wait.until(EC.presence_of_element_located(('id', 'form_item_login')))
login_form.send_keys('TEST')
time.sleep(0.5)
login_form.clear()
login_form.send_keys(os.getenv('LOGIN'))

password_form = driver.find_element('id', 'form_item_password')
password_form.send_keys(os.getenv('PASSWORD'))

auth_button = driver.find_element('xpath', "//button//span[text()='Войти']")
auth_button.click()

print(driver.current_url)


input('Press Enter to end')
driver.quit()
