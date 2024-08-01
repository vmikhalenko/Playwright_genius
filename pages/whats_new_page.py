from pages.base_page import BasePage
from pages.locators import whats_new_locators as loc
from playwright.sync_api import expect
import allure

class WhatsNew(BasePage):
    page_url = '/what-is-new.html'

    @allure.step('Click the button')
    def click_shop_the_yoga_button(self):
        self.find(loc.shop_new_yoga_button).click()

    @allure.step('Check that correct page is opened')
    def check_that_correct_url_is_opened(self):
        expect(self.page).to_have_url('https://magento.softwaretestingboard.com/collections/yoga-new.html')
