from pages.base_page import BasePage
from pages.locators import product_page_locators as loc
from playwright.sync_api import Page, expect
import allure

class ProductPage(BasePage):
    page_url = '/olivia-1-4-zip-light-jacket.html'

    @allure.step('Add product to cart')
    def adding_one_product_to_cart(self,counter_number):
        size = self.find(loc.size).click()
        color = self.find(loc.color).click()
        button = self.find(loc.button).click()
        counter = self.find(loc.counter)
        expect(counter).to_have_text(counter_number)
