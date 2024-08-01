from pages.base_page import BasePage
from pages.locators import drop_menu_locators as loc
from playwright.sync_api import expect
import allure

class HomePage(BasePage):
    page_url = '/'

    @allure.step('Open the home page')
    def drop_menu(self,text):
        women = self.find(loc.women)
        tops = self.find(loc.tops)
        jackets = self.find(loc.jackets)
        women.hover()
        tops.hover()
        jackets.click()
        jackets_header = self.find(loc.jackets_header)
        expect(jackets_header).to_have_text(text)
