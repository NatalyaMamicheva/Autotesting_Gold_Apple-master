import datetime
import os
from pathlib import Path

from selenium.webdriver import ActionChains


class Base:
    """Базовый класс с общими методами для каждой страницы"""
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def get_current_url(self):
        """Метод получения url"""
        get_url = self.driver.current_url
        print(f'Получен url: {get_url}')

    @staticmethod
    def get_assert_word(word, result):
        """Метод проверки слов"""
        value_word = word.text
        assert value_word == result
        print('ОК')

    def get_screenshot(self):
        """Метод скриншот"""
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M")
        screenshot = f'screenshot{now_date}.png'
        project_path = Path(os.getcwd())
        self.driver.save_screenshot(f'{project_path}\\screen\\' + screenshot)
