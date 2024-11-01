import httpx
from jsonschema import validate
from core.contracts import USER_DATA_SCHEMA
import allure

BASE_URL = 'https://reqres.in/'
LIST_USERS = 'api/users?page=2'
SINGLE_USER = 'api/users/2'
SINGLE_USER_NOT_FOUND = 'api/users/23'
EMAIL_ENDS = '@reqres.in'
AVATAR_ENDS = '-image.jpg'
DELAYED_REQUEST = 'api/users?delay=3'

@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем получение списка пользователей')
def test_list_users():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + LIST_USERS}'):
    # response = httpx.get("https://reqres.in/api/users?page=2")
        response = httpx.get(BASE_URL + LIST_USERS)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    data = response.json()['data']
    # validate(data, USER_DATA_SCHEMA)
    for item in data:
        with allure.step('Проверяем элемент из списка'):
            validate(item, USER_DATA_SCHEMA)
            with allure.step('Проверяем окончание EMAIL адреса'):
                assert item["email"].endswith(EMAIL_ENDS)
            # assert str(item["id"]) in item["avatar"]
            with allure.step('Проверяем наличие id в ссылке на аватарку'):
                assert item["avatar"].endswith(str(item["id"]) + AVATAR_ENDS)

    # print(response)
    # print(response.text)
    # print(response.json()['data'])

@allure.suite('Проверка запросов данных пользователя')
@allure.title('Проверяем получение данных пользователя')
def test_single_user():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + SINGLE_USER}'):
        response = httpx.get(BASE_URL + SINGLE_USER)
    assert response.status_code == 200
    data = response.json()['data']

    with allure.step('Проверяем окончание EMAIL адреса'):
        assert data["email"].endswith(EMAIL_ENDS)
    with allure.step('Проверяем наличие id в конце аватарки'):
        assert data["avatar"].endswith(str(data["id"]) + AVATAR_ENDS)

@allure.suite('Проверка запроса отсутствующего пользователя')
@allure.title('Проверяем получение отсутствующего пользователя')
def test_user_not_found():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + SINGLE_USER_NOT_FOUND}'):
        response = httpx.get(BASE_URL + SINGLE_USER_NOT_FOUND)
    assert response.status_code == 404

def test_delayed_user_list():
    response = httpx.get(BASE_URL + DELAYED_REQUEST, timeout=4)
    assert response.status_code == 200

