import pytest
from courier_generator import register_new_courier_and_return_login_password, generate_login_pass


@pytest.fixture
def new_courier():
    login, password, firstname = generate_login_pass()
    payload = {
        "login": login,
        "password": password,
        "firstName": firstname
    }
    yield payload


@pytest.fixture
def existed_courier():
    login, password, firstname = register_new_courier_and_return_login_password()
    payload = {
        'login': login,
        'password': password,
        'firstName': firstname
    }
    yield payload
