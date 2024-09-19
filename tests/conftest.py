import pytest


@pytest.fixture()
def set_up():
    print('Начало теста')
    yield
    print('Конец теста')


@pytest.fixture(scope="module")
def set_group():
    print('Вход в систему')
    yield
    print('Выход из системы')
