import pytest
import allure

@allure.feature('Header text')
@pytest.mark.regression
def test_header_text(sale_page):
    sale_page.open_page()
    sale_page.check_page_header('Sale')
