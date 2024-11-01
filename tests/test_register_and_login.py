import json

import httpx
import pytest
from jsonschema import validate
from core.contracts import REGISTERED_USER_SCHEME, UNREGISTERED_USER_SCHEME, LOGINED_USER_SCHEME

BASE_URL = 'https://reqres.in/'
REGISTER_USER = 'api/register'
LOGIN_USER = 'api/login'

json_file = open('/Users/id/PycharmProjects/TestPythonProject/core/new_users_data.json')
users_data = json.load(json_file)
error_json_file = open('/Users/id/PycharmProjects/TestPythonProject/core/error_users_data.json')
error_users_data = json.load(error_json_file)

@pytest.mark.parametrize('users_data', users_data)
def test_succesful_register(users_data):
    headers = {'Content-Type': 'application/json'}
    response = httpx.post(BASE_URL + REGISTER_USER, json=users_data, headers=headers)
    print(users_data)
    assert response.status_code == 200
    validate(response.json(), REGISTERED_USER_SCHEME)

@pytest.mark.parametrize('error_users_data', error_users_data)
def test_unsuccesful_register(error_users_data):
    response = httpx.post(BASE_URL + REGISTER_USER, json=error_users_data)
    assert response.status_code == 400
    validate(response.json(), UNREGISTERED_USER_SCHEME)

@pytest.mark.parametrize('users_data', users_data)
def test_succesful_login(users_data):
    response = httpx.post(BASE_URL + LOGIN_USER, json=users_data)
    print(users_data)
    assert response.status_code == 200
    validate(response.json(), LOGINED_USER_SCHEME)
