from pages.base_page import BasePage
from pages.locators import sale_page_locators as loc
from playwright.sync_api import expect
import allure


class SalePage(BasePage):
    page_url = '/sale.html'

    @allure.step('Check header text')
    def check_page_header(self,text):
        header_text = self.find(loc.header_text_locator)
        expect(header_text).to_have_text(text)