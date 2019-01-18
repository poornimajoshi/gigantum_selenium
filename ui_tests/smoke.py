from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_page_load_timeout(10)
driver.get("http://localhost:10000/")
delay = 5

# Click on login button

try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.Login_button')))
except TimeoutException:
    print('Either page did not load or login button was not found')
driver.find_element_by_class_name('Login__button').click()

# Enter username and password
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'auth0-lock-cred-pane auth0-lock-quiet')))
except TimeoutException:
    print('Username login page not found')
driver.find_element_by_css_selector("input.auth0-lock-input[name='username']").send_keys('poornimajoshi')
driver.find_element_by_css_selector("input.auth0-lock-input[name='password']").send_keys('marnIpoo@23')
driver.find_element_by_class_name('auth0-lock-submit').click()
driver.implicitly_wait(8)
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//div[@class='btn--import'][contains(text(),'Create New')]")))
except TimeoutException:
    print('Create New button was not visible')
driver.find_element_by_xpath("//div[@class='btn--import'][contains(text(),'Create New')]").click()

driver.find_element_by_xpath("//input[@placeholder='Enter a unique, descriptive title']").send_keys("a-plot-for-emmys")
driver.find_element_by_xpath("//textarea[contains(@placeholder,'Briefly describe this Project, its purpose and any other key details.')]").send_keys("A simple demo")
driver.find_element_by_xpath("//button[contains(text(),'Continue')]").click()

driver.implicitly_wait(3)

# Selecting the python project type and Creating the project
driver.find_element_by_xpath("//h6[contains(text(),'Python3 Minimal')]").click()
driver.find_element_by_xpath("//button[contains(@class,'ButtonLoader')]").click()
