import pytest
import requests
import allure
from URL import *
from data import order_payload


class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа с разными комбинациям заполнения поля "цвет"')
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    def test_create_order(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "pytest tests.py --allure dir=allure_results Saske, come back to Konoha",
            "color": color
        }
        response = requests.post(ORDERS_URL, params=payload)
        assert response.status_code == 201 and "track" in response.text
