import pytest
from pages.login_page import login_page
from test_cases.BaseTest import BaseTest
from utilities import data_provider
import logging
from utilities.log_utility import logger



log = logger(__name__,logging.INFO)

class Test_login(BaseTest):

    @pytest.mark.parametrize("email,password", data_provider.get_data("Sheet1"))
    def test_do_login(self, email, password):
        log.logger.info("Test Do login started")

        log_in_page = login_page(self.driver)
        log_in_page.enter_crendentials(email, password)

        log.logger.info("Test login successfully executed")


