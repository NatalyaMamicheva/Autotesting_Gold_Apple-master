import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.logger import Logger


class GeoPage(Base):
    """Класс настройки геолокации"""

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://goldapple.ru/'
        self.delivery_address = '//aside[@class="ga-header__location-confirm-address"]'
        self.button_no = '//span[contains(text(),"Нет, другой")]'
        self.button_yes = '//span[contains(text(),"Да, верно")]'
        self.city = './/div[@data-test-id="city-select"]/../button'
        self.country_all = '//div[@class="ga-select__box-content"]'
        self.country = '//span[contains(text(),"Россия")]'
        self.find_city = '//input[@placeholder="Найти город"]'
        self.my_city = '(//em[contains(text(),"Самара")])[1]'
        self.find_street = '(//input[@data-test-id="input"])[2]'
        self.bring_button = '//span[contains(text(),"привезти сюда")]'

    def get_delivery_address(self):
        """Проверка наличия окна подтверждения геолокации"""
        if WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_address))):
            return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, self.delivery_address))))
        else:
            return None

    def get_button_no(self):
        """Получение кнопки нет"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.button_no))))

    def get_button_yes(self):
        """Получение кнопки да"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.button_yes))))

    def click_button_no(self):
        """Нажатие кнопки нет"""
        self.get_button_no().click()
        print('Заполнение адреса доставки')

    def click_button_yes(self):
        """Нажатие кнопки да"""
        self.get_button_yes().click()
        print('Переход на главную страницу')

    def get_city(self):
        """Получение окна города"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.city))))

    def get_country_all(self):
        """Получение всех стран"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.country_all))))

    def get_country(self):
        """Получение одной конкретной страны"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.country))))

    def get_find_city(self):
        """Получение окна с выбором города"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.find_city))))

    def get_my_city(self):
        """Получение одного конкретного города"""
        return (WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, self.my_city))))

    def get_find_street(self):
        """Получение окна улицы"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.find_street))))

    def get_bring_button(self):
        """Получение кнопки подтверждения адреса поиска товаров"""
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.bring_button))))

    def click_city(self):
        """Нажатие на окно города"""
        self.get_city().click()

    def click_country_all(self):
        """Нажатие на список стран"""
        self.get_country_all().click()

    def click_country(self):
        """Нажатие на выбранную страну"""
        self.get_country().click()
        print('Выбор страны')

    def send_find_city(self):
        """Написание требуемого города в окно"""
        self.get_find_city().send_keys('Самара')

    def click_find_city(self):
        """Нажатие на выбранный город"""
        time.sleep(3)
        self.get_my_city().click()
        time.sleep(3)
        print('Выбор города')

    def click_find_street(self):
        """Нажатие на окно ввода улицы"""
        self.get_find_street().click()

    def send_find_street(self):
        """Ввод требуемой улицы и дома"""
        print(self.get_find_street().text)
        self.actions.move_to_element(self.get_find_street()).perform()
        self.get_find_street().send_keys('Травяная 47')

    def click_street(self):
        """Нажатие на выбранную улицу и дом"""
        value = (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@class="ga-location-street-house-select__option"]/../../li[1]'))))
        value.click()
        print('Выбор улицы и номера дома')

    def click_bring_button(self):
        """Нажатие на кнопку подтверждения адреса"""
        self.get_bring_button().click()
        print('Выбран адрес для поиска товаров')

    def check(self):
        """Проверка на наличие окна геолокации и дальнейший вызов всех методов"""
        if self.get_delivery_address() is not None:
            # self.click_button_yes()
            self.click_button_no()
            self.click_city()
            self.click_country_all()
            self.click_country()
            self.send_find_city()
            self.click_find_city()
            self.click_find_street()
            self.send_find_street()
            self.click_street()
            self.click_bring_button()
        else:
            print('Геолокация определена успешно')

    def enter(self):
        """Открытие сайта и запуск методов"""
        with allure.step('Enter'):
            Logger.add_start_step(method='enter')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.check()
            Logger.add_end_step(self.driver.current_url, method='enter')
