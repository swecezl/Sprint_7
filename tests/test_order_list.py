import pytest
import requests
import allure
from URL import *


class TestOrderList:
    @allure.title('Проверка возврата списка заказов')
    def test_order_list(self):
        response = requests.get(ORDERS_URL)
        assert "orders" in response.json() and response.json()["orders"] is not None
