from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://en.wikipedia.org/wiki/Selenium')

waiting = WebDriverWait(driver, 10)

links = waiting.until(expected_conditions.presence_of_all_elements_located((By.TAG_NAME,"a")))

for i in links:
    print(i.text,i.get_attribute('href'))