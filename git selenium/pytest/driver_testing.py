import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeservice
from webdriver_manager.chrome import ChromeDriverManager

def get_data():
    return[
        ('apple','pandu'),
        ('banana','pandu')
    ]


def setup_module():
    global driver
    driver = webdriver.Chrome(service=chromeservice(ChromeDriverManager().install()))
    print('apple')
    


def teardown_module():
    driver.quit()
    print('apple quit')


@pytest.mark.parametrize('username,password',get_data())
def test_do_login(username, password):
    driver.get('https://google.com')
    print(username, '---', password)

def test_facebook():
    driver.get('https://facebook.com')