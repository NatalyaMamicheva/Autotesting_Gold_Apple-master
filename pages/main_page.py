import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.logger import Logger


class MainPage(Base):
    """Класс страницы со всеми товарами"""

    def __init__(self, driver):
        super().__init__(driver)
        self.catalog = '(//span[contains(text(),"каталог")])[1]'
        self.make_up = '//span[contains(text(),"макияж")]'
        self.lips = '(//span[contains(text(),"губы")])[2]'
        self.filters = '//button[@data-transaction-name="ga-filters-toggle"]'
        self.in_stoke = './/input[@name="storestocks"]/..'
        self.min_price_button = '//div[contains(text()," от ")]/../../div[2]/button[1]'
        self.max_price_button = '//div[contains(text()," от ")]/../../div[2]/button[2]'
        self.type_product = '//div[contains(text(),"тип продукта")]'
        self.button_select_product = '//span[contains(text(),"Показать")]'
        self.catalog_view = '//div[contains(text(),"вид каталога")]'
        self.product = '//a[@href="/14019300004-eclat-minute"]'

    def get_catalog(self):
        """Получение элемента каталог"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.catalog))))

    def click_catalog(self):
        """Нажатие на элемент каталога"""
        self.get_catalog().click()
        print('Открыт каталог')

    def get_make_up(self):
        """Получение элемента макияж"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.make_up))))

    def click_make_up(self):
        """Нажатие на элемент макияж"""
        self.get_make_up().click()
        print('Открыт раздел макияжа')

    def get_lips(self):
        """Получение элемента губы"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.lips))))

    def click_lips(self):
        """Нажатие на элемент губы"""
        self.get_lips().click()
        print('Открыт раздел губы')

    def get_filters(self):
        """Открытие фильтров"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.filters))))

    def get_in_stoke(self):
        """Фильтр в наличии"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.in_stoke))))

    def get_min_price_button(self):
        """Фильтр минимальной цены"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.min_price_button))))

    def get_max_price_button(self):
        """Фильтр максимальной цены"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.max_price_button))))

    def get_type_product(self):
        """Фильтр типа продукта"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.type_product))))

    def get_select_product(self):
        """Кнопка показать продукты после применения фильтров"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.button_select_product))))

    def get_product(self):
        """Товар"""
        my_product = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.product)))
        self.actions.move_to_element(my_product).perform()
        return my_product

    def click_filters(self):
        """Нажатие на элемент фильтры"""
        scroll_origin = ScrollOrigin.from_element(self.get_filters())
        ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, 200).perform()
        time.sleep(3)
        self.get_filters().click()
        print('Открыт фильтр категории для губ')

    def click_in_stoke(self):
        """Нажатие на фильтр в наличии"""
        self.get_in_stoke().click()
        print('Нажат фильтр в наличии')

    def click_min_price_button(self):
        """Нажат фильтр минимальной цены"""
        self.actions.click_and_hold(self.get_min_price_button()).move_by_offset(50, 0).release().perform()
        print('Нажат фильтр минимальной цены')

    def click_max_price_button(self):
        """Нажат фильтр максимальной цены"""
        self.actions.click_and_hold(self.get_max_price_button()).move_by_offset(-100, 0).release().perform()
        print('Нажат фильтр максимальной цены')

    def click_type_product(self):
        """Нажат фильтр типа продукта"""
        bottom_element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[contains(text(),"финиш")]')))
        self.actions.move_to_element(bottom_element).perform()
        self.get_type_product().click()
        all_type = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//span[contains(text(),"показать все")]')))
        all_type.click()
        find_lip = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//input[@name="filter-search"]')))
        find_lip.send_keys('бле')
        lip_gloss = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//span[contains(text(),"блеск для губ")]')))
        lip_gloss.click()
        print('Нажат фильтр типа продукта')

    def click_select_product(self):
        """Нажата кнопка показать продукты после применения фильтров"""
        self.get_select_product().click()
        print('Нажата кнопка показать продукты после применения фильтров')

    def get_catalog_view(self):
        """Кнопка вида ячеек с товарами"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.catalog_view))))

    def click_catalog_view(self):
        """Нажата кнопка вида ячеек с товарами"""
        self.get_catalog_view().click()
        print('Нажата кнопка вида ячеек с товарами')

    def click_product(self):
        """Выбран товар"""
        self.get_product().click()
        print('Выбран товар')

    def select_product(self):
        """Выбор продукта для покупки"""
        with allure.step('Select Product'):
            Logger.add_start_step(method='select_product')
            self.get_current_url()
            self.click_catalog()
            self.click_make_up()
            self.click_lips()
            self.click_filters()
            self.click_in_stoke()
            self.click_min_price_button()
            self.click_max_price_button()
            self.click_type_product()
            self.click_select_product()
            self.click_catalog_view()
            self.click_product()
            Logger.add_end_step(self.driver.current_url, method='select_product')
