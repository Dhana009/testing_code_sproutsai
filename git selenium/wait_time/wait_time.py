from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

normal_wait = WebDriverWait(driver, 10)  # waits for 10 seconds

#case 1 : element_to_be_clickable
driver.get('http://the-internet.herokuapp.com/dynamic_loading/1')
print("Before clicking the Start button")
start_element = normal_wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="start"]/button')))
start_element.click()
print("After clicking the Start button")

#case 2 : visibility_of_element_located
after_element = normal_wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="finish"]')))
print(after_element.text)

#case 3 : text_to_be_present_in_element
driver.get('http://the-internet.herokuapp.com/dynamic_loading/1')
start_element = normal_wait.until(EC.text_to_be_present_in_element((By.XPATH, '//div[@id="start"]/button'),'Start'))
if start_element:
    print('yes')


#case 4 : title contains
driver.get('http://the-internet.herokuapp.com/dynamic_loading/1')
start_element = normal_wait.until(EC.title_contains('The Internet'))
if start_element:
    print('yes')

#wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'element_class')))
#wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'element_tag')))
#wait.until(EC.invisibility_of_element_located((By.ID, 'element_id')))



