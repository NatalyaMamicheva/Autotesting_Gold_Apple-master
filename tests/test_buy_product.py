import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from pages.geo_page import GeoPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.payment_page import PaymentPage

@allure.description('Test Buy Product')
def test_buy_product(set_up, set_group):
    """Тест по прохождению бизнес-пути покупки товара на сайте Золотое Яблоко"""
    options = Options()
    options.page_load_strategy = 'eager'
    options.add_experimental_option("detach", True)
    options.add_argument('--ignore-certificate-errors-spki-list')
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print('Открытие браузера')

    gp = GeoPage(driver)
    print('Работа с окнами подтверждения геолокации')
    gp.enter()

    mp = MainPage(driver)
    print('Переход на страницу со всеми товарами')
    mp.select_product()

    pp = ProductPage(driver)
    print('Переход на страницу с выбранным товаром')
    pp.ok_product()

    pape = PaymentPage(driver)
    print('Переход на страницу оплаты товара')
    pape.buy_product()
