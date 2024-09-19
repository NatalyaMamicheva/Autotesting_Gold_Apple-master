import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.logger import Logger


class PaymentPage(Base):
    """Класс страницы оплаты товара"""

    def __init__(self, driver):
        super().__init__(driver)
        self.type_delivery = '(//button[@class="inline-tabs-item"])[1]'
        self.flat = '(//input[@name="flat"])[1]'
        self.intercom_code = '(//input[@name="intercom_code"])[1]'
        self.entrance = '(//input[@name="entrance"])[1]'
        self.floor = '(//input[@name="floor"])[1]'
        self.delivery_button = '(//span[contains(text(),"Привезти сюда")])[2]'
        self.day = '//div[@class="datepicker__oval-dates"]/div[4]'
        self.time = '(//div[@class="inline-select__option-inner"])[1]'
        self.my_time = '(//div[@class="inline-select__option-inner"])[3]'
        self.lastname = '//input[@name="lastname"]'
        self.firstname = '//input[@name="firstname"]'
        self.middlename = '//input[@name="middlename"]'
        self.telephone = '//input[@name="telephone"]'
        self.email = '//input[@name="email"]'
        self.checkbox = '(//span[@class="checkbox-field__input-icon"])[1]'

    def get_type_delivery(self):
        """Кнопка доставки курьером"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.type_delivery)))

    def get_flat(self):
        """Квартира"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.flat)))

    def get_intercom_code(self):
        """Домофон"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.intercom_code)))

    def get_entrance(self):
        """Подъезд"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.entrance)))

    def get_floor(self):
        """Этаж"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.floor)))

    def get_delivery_button(self):
        """Кнопка подтверждения адреса"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.delivery_button)))

    def get_day(self):
        """Кнопка дня заказа"""
        day = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.day)))
        bottom = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[contains(text(),"Контакты")]')))
        self.actions.move_to_element(bottom).perform()
        return day

    def get_time(self):
        """Кнопка времени заказа"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.time))))

    def get_my_time(self):
        """Выбранная кнопка времени заказа"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.my_time))))

    def get_lastname(self):
        """Фамилия"""
        my_lastname = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.lastname)))
        bottom = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//h5[contains(text(),"Оплата")]')))
        self.actions.move_to_element(bottom).perform()
        return my_lastname

    def get_firstname(self):
        """Имя"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.firstname)))

    def get_middlename(self):
        """Отчество"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.middlename)))

    def get_telephone(self):
        """Номер телефона"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.telephone)))

    def get_email(self):
        """Электронная почта"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.email)))

    def get_checkbox(self):
        """Чек-бокс согласия с условиями"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.checkbox)))

    def get_pay(self):
        """Способы оплаты товара"""
        bottom = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@class="footer__checkout-contact-title"]')))
        self.actions.move_to_element(bottom).perform()

    def click_type_delivery(self):
        """Нажата кнопка доставки курьером"""
        self.get_type_delivery().click()
        print('Нажата кнопка доставки курьером')

    def send_flat(self):
        """Заполнена квартира"""
        self.get_flat().send_keys('4')

    def send_intercom_code(self):
        """Заполнен домофон"""
        self.get_intercom_code().send_keys('4')

    def send_entrance(self):
        """Заполнен подъезд"""
        self.get_entrance().send_keys('1')

    def send_floor(self):
        """Заполнен этаж"""
        self.get_floor().send_keys('1')

    def click_delivery_button(self):
        """Нажата кнопка подтверждения адреса"""
        self.get_delivery_button().click()
        print('Нажата кнопка подтверждения адреса')

    def click_day(self):
        """Нажата кнопка дня заказа"""
        self.get_day().click()
        print('Нажата кнопка дня заказа')

    def click_time(self):
        """Нажата кнопка времени заказа"""
        self.actions.click_and_hold(self.get_time()).move_by_offset(-200, 0).release().perform()
        print('Нажата кнопка времени заказа')

    def click_my_time(self):
        """Нажата выбранная кнопка времени заказа"""
        self.get_my_time().click()
        print('Нажата выбранная кнопка времени заказа')

    def send_data_buyer(self):
        """Заполнены данные о покупателе"""
        self.get_lastname().send_keys('Мамичева')
        self.get_firstname().send_keys('Наталья')
        self.get_middlename().send_keys('Дмитриевна')
        self.get_telephone().send_keys('9998161121')
        self.get_email().send_keys('mymail989898@mail.ru')
        print('Заполнены данные о покупателе')

    def click_checkbox(self):
        """Нажат чек-бокс согласия с условиями"""
        self.get_checkbox().click()
        print('Нажат чек-бокс согласия с условиями')

    def buy_product(self):
        """Покупка товара"""
        with allure.step('Buy Product'):
            Logger.add_start_step(method='buy_product')
            self.get_current_url()
            self.click_type_delivery()
            self.send_flat()
            self.send_intercom_code()
            self.send_entrance()
            self.send_floor()
            self.click_delivery_button()
            self.click_day()
            self.click_time()
            self.click_my_time()
            self.send_data_buyer()
            self.click_checkbox()
            self.get_pay()
            print("Заказ оформлен успешно! Осталось лишь оплатить его на сайте одного из наших партнеров")
            time.sleep(3)
            self.get_screenshot()
            Logger.add_end_step(self.driver.current_url, method='buy_product')