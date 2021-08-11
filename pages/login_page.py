from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Can't find word 'login' in url"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        # принимает две строки и регистрирует пользователя
        self.go_to_login_page()
        self.should_be_register_form()
        self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_FIELD_IN_REGISTRATION_FORM).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_IN_REGISTRATION_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD_IN_REGISTRATION_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()



