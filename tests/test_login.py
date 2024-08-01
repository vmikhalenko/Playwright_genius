import pytest
import allure

@allure.feature('Sign in')
@pytest.mark.smoke
def test_incorrect_login(login_page):
    login_page.open_page()
    login_page.fill_login_form('john@mail.com','fgdgdgerger')
    login_page.check_error_alert_text(
        'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    )