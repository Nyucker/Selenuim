from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.3')

driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)

driver.get('https://the-internet.herokuapp.com/dynamic_controls')

# visible_after = ("xpath", "//button[@id='visibleAfter']")
# button = wait.until(EC.visibility_of_element_located(visible_after))
# button.click()

enable_after = ("xpath", "//button[text()='Enable']")
wait.until(EC.element_to_be_clickable(enable_after)).click()

text_field = ('xpath', '//input[@type="text"]')
wait.until(EC.element_to_be_clickable(text_field)).send_keys('<PASSWORD>')


