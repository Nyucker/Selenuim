from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
# options.add_argument('--window-size=1920,1080')
# options.add_argument('disable-blink-features=AutomationControlled')
options.add_argument('--ignore-certificate-errors')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
# driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get('https://demoqa.com/alerts')

button_1 = ('xpath', '//button[@id="alertButton"]')
wait.until(EC.element_to_be_clickable(button_1))

alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
alert.accept()

# driver.quit()