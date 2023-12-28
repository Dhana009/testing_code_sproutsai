from pages.base_page import BasePage



class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fillForm(self, email,password):
        self.type("enter_email_XPATH",email)
        self.type("enter_password_XPATH",password)
        self.click("show_password_XPATH")
        self.click("sign_in_button_XPATH")
