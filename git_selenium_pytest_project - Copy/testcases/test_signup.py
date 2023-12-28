import pytest
from pages.loginpage import login_page
from testcases.BaseTest import BaseTest
from utilities import dataProvider
import logging
from utilities.LogUtil import Logger

log = Logger(__name__,logging.INFO)

class Test_login(BaseTest):

    @pytest.mark.parametrize("email,password", dataProvider.get_data("Sheet1"))
    def test_do_login(self, email, password):
        print("Test method is running!")
        #self.driver.get(config_reader.readconfig_file('basic info', 'home_page'))
        log.logger.info("Test Do login started")
        log_in_page = login_page(self.driver)
        log_in_page.enter_crendentials(email, password)
        log.logger.info("Test login successfully executed")