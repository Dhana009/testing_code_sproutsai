from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from utilities import configReader
import logging
from utilities.LogUtil import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        wait = WebDriverWait(self.driver, 10)

        if str(locator).endswith("_XPATH"):
            wait.until(expected_conditions.element_to_be_clickable((By.XPATH,configReader.readConfig("locators", locator)))).click()
        elif str(locator).endswith("_CSS"):
            wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,configReader.readConfig("locators", locator)))).click()
        elif str(locator).endswith("_ID"):
            wait.until(expected_conditions.element_to_be_clickable((By.ID,configReader.readConfig("locators", locator)))).click()
        
        log.logger.info("Clicking on an element: " + str(locator))




    def type(self, locator,value):
        wait = WebDriverWait(self.driver, 10)

        if str(locator).endswith("_XPATH"):
            wait.until(expected_conditions.element_to_be_clickable((By.XPATH,configReader.readConfig("locators", locator)))).send_keys(value)
        elif str(locator).endswith("_CSS"):
            wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,configReader.readConfig("locators", locator)))).send_keys(value)
        elif str(locator).endswith("_ID"):
            wait.until(expected_conditions.element_to_be_clickable((By.ID,configReader.readConfig("locators", locator)))).send_keys(value)
        
        log.logger.info("Clicking on an element: " + str(locator) + " value entered as : " + str(value))
