from pages.base_page import BasePage
from pages.locators import login_locators as loc
from playwright.sync_api import expect
import allure


class CustomerLogin(BasePage):
    page_url = '/customer/account/login/'

    @allure.step('Enter email, password and click the button')
    def fill_login_form(self,login,password):
        email_field = self.find(loc.email_locator)
        password_field = self.find(loc.password_locator)
        button = self.find(loc.button_locator)
        email_field.fill(login)
        password_field.fill(password)
        button.click()

    @allure.step('Check message')
    def check_error_alert_text(self,text):
        expect(self.page.get_by_role('alert').first).to_have_text(text)