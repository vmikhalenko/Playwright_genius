import pytest
from playwright.sync_api import Page, BrowserContext
from pages.home_page import HomePage
from pages.sale_page import SalePage
from pages.customer_login import CustomerLogin
from pages.whats_new_page import WhatsNew
from pages.product_page import ProductPage


@pytest.fixture()
def page(context:BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width':1920, 'height':1080})
    return page

@pytest.fixture()
def sale_page(page: Page) -> SalePage:
    return SalePage(page)

@pytest.fixture()
def login_page(page: Page) -> CustomerLogin:
    return CustomerLogin(page)

@pytest.fixture()
def product_page(page: Page) -> ProductPage:
    return ProductPage(page)

@pytest.fixture()
def home_page(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture()
def whats_new_page(page: Page) -> WhatsNew:
    return WhatsNew(page)