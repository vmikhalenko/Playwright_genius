import pytest
import allure

@allure.feature('Drop-menu move')
@pytest.mark.regression
def test_drop_menu_move_to_page(home_page):
    home_page.open_page()
    home_page.drop_menu('Jackets')
