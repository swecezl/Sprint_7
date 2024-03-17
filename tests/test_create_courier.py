import pytest
import requests
import allure
from URL import CREATE_COURIER_URL
from courier_generator import generate_login_pass
from data import *


class TestCreateCourier:
    @allure.title('Проверка успешного создания учетной записи курьера')
    def test_create_new_courier_is_ok(self, new_courier):
        payload = new_courier
        response = requests.post(CREATE_COURIER_URL, data=payload)
        assert response.status_code == 201 and response.text == create_courier_is_ok_text

    @allure.title('Проверка невозможности создания курьеров с одинаковыми данными')
    def test_create_same_courier_error(self, new_courier):
        payload = new_courier
        requests.post(CREATE_COURIER_URL, data=payload)
        response = requests.post(CREATE_COURIER_URL, data=payload)
        assert response.status_code == 409 and response.text == same_courier_error_text

    @allure.title('Проверка невозможности создать учетную записть курьера без заполнения обязательных полей логина/пароля')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_create_courier_without_required_fields(self, field):
        login, password, firstname = generate_login_pass()
        payload = {
            'login': login,
            'password': password,
            'firstname': firstname
        }
        del payload[field]
        response = requests.post(CREATE_COURIER_URL, data=payload)
        assert response.status_code == 400 and response.text == create_courier_without_required_field_error_text

