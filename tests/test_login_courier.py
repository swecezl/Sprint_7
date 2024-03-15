import pytest
import requests
import allure
from URL import LOGIN_URL
from data import *


class TestLogin:
    @allure.title('Проверка получения id при успешном логине курьера')
    def test_login(self, existed_courier):
        payload = existed_courier
        response = requests.post(LOGIN_URL, data=payload)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверка невозможности логина без заполнения обязательных полей логина/пароля')
    @pytest.mark.parametrize('field, status, text',
                             [("login", 400, login_courier_without_login_error_text),
                              ("password", 504, 'Service unavailable')])
    def test_login_without_required_fields(self, existed_courier, field, status, text):
        payload = existed_courier
        del payload[field]
        response = requests.post(LOGIN_URL, data=payload)
        assert response.status_code == status and response.text == text

    @allure.title('Проверка невозможности логина с допущенными ошибками в логине/пароля зарегестрированного курьера')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_invalid_login_or_password(self, existed_courier, field):
        payload = existed_courier
        payload[field] += 'add_invalid_creds'
        response = requests.post(LOGIN_URL, data=payload)
        assert response.status_code == 404 and response.text == login_invalid_creds

    @allure.title('Проверка невозможности логина незарегестрированного курьера')
    def test_login_unregistered_courier(self, new_courier):
        login, password, firstname = new_courier
        payload = {
            'login': login,
            'password': password,
            'firstName': firstname
        }
        response = requests.post(LOGIN_URL, data=payload)
        assert response.status_code == 404 and response.text == login_invalid_creds


