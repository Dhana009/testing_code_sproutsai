from pages.basepage import BasePage
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest

class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fillForm(self, email,password):
        self.type("enter_email_XPATH",email)
        self.type("enter_password_XPATH",password)
        self.click("show_password_XPATH")
        self.click("sign_in_button_XPATH")
        try:
            # Wait for 10 seconds after clicking "Sign In"
            time.sleep(6)

            # Check if "Post new job" is present in the page source
            if "Post new job" not in self.driver.page_source:
                raise Exception("Post new job not found in the page source")

            self.click("logout_button_menu_XPATH")
            self.click('logout_button_XPATH')
            time.sleep(2)
            

        except Exception as e:
            self.driver.refresh()
            pytest.fail("Test failed: Post new job not found after logout")

