import httpx
from jsonschema import validate
from core.contracts import CREATE_USER_SCHEME
from core.contracts import UPDATE_USER_SCHEME
import datetime
import allure

BASE_URL = 'https://reqres.in/'
CREATE_USER = 'api/users'
UPDATE_USER = 'api/users/2'
DELETE_USER = 'api/users/2'

@allure.suite('Проверка запроса на создание пользователя')
@allure.title('Проверяем создание пользователя')
def test_create_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "leader"
    }
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + CREATE_USER}'):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())

    with allure.step('Проверяем пользователя'):
        validate(response_json, CREATE_USER_SCHEME)
        with allure.step('Проверяем соответствие имени'):
            assert response_json['name'] == body['name']
        with allure.step('Проверяем соответствие работы'):
            assert response_json['job'] == body['job']
        with allure.step('Проверяем соответствие времени создания'):
            assert creation_date[0:16] == current_date[0:16]

@allure.suite('Проверка запроса на создание пользователя без имени')
@allure.title('Проверяем создание пользователя без имени')
def test_create_user_without_name():
    body = {
        "job": "leader"
    }
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + CREATE_USER}'):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())

    with allure.step('Проверяем пользователя'):
        validate(response_json, CREATE_USER_SCHEME)
        with allure.step('Проверяем соответствие работы'):
            assert response_json['job'] == body['job']
        with allure.step('Проверяем соответствие времени создания'):
            assert creation_date[0:16] == current_date[0:16]

@allure.suite('Проверка запроса на создание пользователя без работы')
@allure.title('Проверяем создание пользователя без работы')
def test_create_user_without_job():
    body = {
        "name": "morpheus"
    }
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + CREATE_USER}'):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, CREATE_USER_SCHEME)
    with allure.step('Проверяем соответствие имени'):
        assert response_json['name'] == body['name']
    with allure.step('Проверяем соответствие времени создания'):
        assert creation_date[0:16] == current_date[0:16]


@allure.suite('Проверка запроса на обновление пользователя')
@allure.title('Проверяем обновление пользователя')
def test_update_user():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + UPDATE_USER}'):
        response = httpx.put(BASE_URL + UPDATE_USER, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    response_json = response.json()
    update_date = response_json['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, UPDATE_USER_SCHEME)
    with allure.step('Проверяем соответствие имени'):
        assert response_json['name'] == body['name']
    with allure.step('Проверяем соответствие работы'):
        assert response_json['job'] == body['job']
    with allure.step('Проверяем соответствие времени создания'):
        assert update_date[0:16] == current_date[0:16]

@allure.suite('Проверка запроса на удаление пользователя')
@allure.title('Проверяем удаление пользователя')
def test_delete_user():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + DELETE_USER}'):
        response = httpx.delete(BASE_URL + DELETE_USER)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 204
