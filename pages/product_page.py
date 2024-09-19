import allure
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.logger import Logger


class ProductPage(Base):
    """Класс страницы товара"""

    def __init__(self, driver):
        super().__init__(driver)
        self.color_all = '//span[@class="ga-select__box-content-value"]/div'
        self.my_color = '//div[contains(text(),"02, apricot shimmer")]'
        self.product_button = '//span[contains(text(),"добавить в корзину")]'
        self.button_cart = '//div[@class="ga-header__tabs"]/button[5]'
        self.button_order = '//span[contains(text(),"Оформить заказ")]'
        self.button_guest = '//span[contains(text(),"продолжить как гость")]'

    def get_all_color(self):
        """Получение элемента макияж"""
        all_color = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.color_all)))
        self.actions.move_to_element(all_color).perform()
        return all_color

    def get_color(self):
        """Требуемый цвет"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.my_color))))

    def get_product_button(self):
        """Выбор продукта"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.product_button)))

    def get_button_cart(self):
        """Кнопка корзина"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.button_cart)))

    def get_button_order(self):
        """Кнопка подтверждения заказа"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.button_order)))

    def get_button_guest(self):
        """Кнопка гостя"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.button_guest)))

    def click_color(self):
        """Открыт список всех оттенков"""
        self.get_all_color().click()
        print('Открыт список всех оттенков')

    def click_my_color(self):
        """Нажат требуемый цвет"""
        self.get_color().click()
        print('Нажат требуемый цвет')

    def click_product_button(self):
        """Нажата кнопка выбора продукта"""
        scroll_origin = ScrollOrigin.from_element(self.get_product_button())
        self.actions.scroll_from_origin(scroll_origin, 0, 200).perform()
        self.get_product_button().click()
        print('Нажата кнопка выбора продукта')

    def click_button_cart(self):
        """Нажата кнопка корзина"""
        self.get_button_cart().click()
        print('Нажата кнопка корзина')

    def click_button_order(self):
        """Нажата кнопка подтверждения заказа"""
        title_name = (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//h1/a')))).text
        title_product = (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//h1/span')))).text
        cart_product = (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//span[@aria-label="CLARINS natural lip perfector"]'))))
        product_price = (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@itemprop="priceSpecification"]/div'))))
        cart_price = (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//span[contains(text(),"Итого")]/../../dt[2]/div/div/div')))).text
        self.get_assert_word(cart_product, f"{title_name} {title_product}")
        self.get_assert_word(product_price, cart_price)
        self.get_button_order().click()
        print('Нажата кнопка подтверждения заказа')

    def click_button_guest(self):
        """Нажата кнопка гостя"""
        self.get_button_guest().click()
        print('Нажата кнопка гостя')

    def ok_product(self):
        """Фильтр товара"""
        with allure.step('Ok Product'):
            Logger.add_start_step(method='ok_product')
            self.get_current_url()
            self.click_color()
            self.click_my_color()
            self.click_product_button()
            self.click_button_cart()
            self.click_button_order()
            self.click_button_guest()
            Logger.add_end_step(self.driver.current_url, method='ok_product')
