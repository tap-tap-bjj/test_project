
from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):

    def register_new_user(self, email, pasword):
        self.should_be_login_url()
        #self.go_to_login_page()
        self.try_find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(email)
        self.try_find_element(*LoginPageLocators.LOGIN_PASWORD1).send_keys(pasword)
        self.try_find_element(*LoginPageLocators.LOGIN_PASWORD2).send_keys(pasword)
        self.try_find_element(*LoginPageLocators.REG_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url # реализуйте проверку на корректный url адрес
        assert 'login' in url, 'Url login не коректно'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login_form отсутствует'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register_form отсутствует'