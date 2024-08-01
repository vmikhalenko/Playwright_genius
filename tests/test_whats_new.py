import pytest
import allure
@allure.feature('URL opening by clicking the button')
@pytest.mark.regression
def test_button(whats_new_page):
    whats_new_page.open_page()
    whats_new_page.click_shop_the_yoga_button()
    whats_new_page.check_that_correct_url_is_opened()