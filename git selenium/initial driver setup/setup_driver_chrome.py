from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeservice
from webdriver_manager.chrome import ChromeDriverManager

chrome_browser = webdriver.Chrome(service=chromeservice(ChromeDriverManager().install()))

chrome_browser.get('https://google.com')

input()