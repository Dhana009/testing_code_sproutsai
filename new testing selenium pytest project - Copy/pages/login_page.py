from pages.base_page import BasePage


class login_page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def enter_crendentials(self,email,password):
        self.type("enter_email",email)
        self.type("enter_password",password)
        self.click('show_password')
        self.click('sign_in_button')