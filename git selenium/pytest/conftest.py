import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeservice
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='module')
def chrome_browser():
    global driver
    driver = webdriver.Chrome(service=chromeservice(ChromeDriverManager().install()))
    yield driver
    driver.quit()