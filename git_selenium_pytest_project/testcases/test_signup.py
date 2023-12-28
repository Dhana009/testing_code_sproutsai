import pytest
from pages.registrationpage import RegistrationPage
from testcases.BaseTest import BaseTest
from utilities import dataProvider
import logging
from utilities.LogUtil import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

log = Logger(__name__,logging.INFO)

class Test_SignUp(BaseTest):

    @pytest.mark.parametrize(" email, password",
                             dataProvider.get_data("Sheet1"))
    def test_doSignUp(self,  email, password):
        log.logger.info("Test Do Sign up started")
        regPage = RegistrationPage(self.driver)
        regPage.fillForm( email, password)
        log.logger.info("Test Do Sign up successfully executed")
        