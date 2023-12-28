import allure
from allure_commons.types import AttachmentType
from requests import request
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as chromeservice
from webdriver_manager.chrome import ChromeDriverManager
from utilities import configReader
import time

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture()
def log_on_failure(request,get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)


#module #class #function #session
@pytest.fixture(params=['chrome'],scope='class')
def get_browser(request):

    if request.param == 'chrome':
        driver = webdriver.Chrome(service=chromeservice(ChromeDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    request.cls.driver = driver
    driver.get(configReader.readConfig("basic info", "google_page"))
    driver.get(configReader.readConfig("basic info", "login_page"))
    driver.maximize_window()
    #driver.implicitly_wait(10)
    
    yield driver

    driver.quit()