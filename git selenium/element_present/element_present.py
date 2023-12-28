from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

normal_wait = WebDriverWait(driver, 1)  # waits for 10 seconds


def element_present(by,how):
    try:
        x = normal_wait.until(EC.visibility_of_element_located((by,how)))
        return x
    except NoSuchElementException or TimeoutException:
        return False
    

driver.get('https://en.m.wikipedia.org/wiki/Selenium')
y = element_present(by=By.XPATH,how='//*[@id="firstHeading"]/spang')
if element_present:
    print(y.text)



