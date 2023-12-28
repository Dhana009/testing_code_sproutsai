from selenium.webdriver.common.by import By
from utilities import config_reader
import logging 
from utilities.log_utility import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

log = logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        wait = WebDriverWait(self.driver, 10)
        try:
            if str(locator).endswith("_XPATH"):
                wait.until(expected_conditions.element_to_be_clickable((By.XPATH,config_reader.readConfig("locators", locator)))).click()
            elif str(locator).endswith("_CSS"):
                wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,config_reader.readConfig("locators", locator)))).click()
            elif str(locator).endswith("_ID"):
                wait.until(expected_conditions.element_to_be_clickable((By.ID,config_reader.readConfig("locators", locator)))).click()
            
            log.logger.info("Clicking on an element: " + str(locator))

        except Exception as e:
            log.logger.error(f'error found while clicking {e}')



    def type(self, locator,value):
        wait = WebDriverWait(self.driver, 10)
        try:
            if str(locator).endswith("_XPATH"):
                wait.until(expected_conditions.element_to_be_clickable((By.XPATH,config_reader.readConfig("locators", locator)))).send_keys(value)
            elif str(locator).endswith("_CSS"):
                wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,config_reader.readConfig("locators", locator)))).send_keys(value)
            elif str(locator).endswith("_ID"):
                wait.until(expected_conditions.element_to_be_clickable((By.ID,config_reader.readConfig("locators", locator)))).send_keys(value)
            
            log.logger.info("Clicking on an element: " + str(locator) + " value entered as : " + str(value))

        except Exception as e:
            log.logger.error(f'error found while clicking {e}')
