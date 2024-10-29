import httpx
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SCHEMA
import allure

BASE_URL = 'https://reqres.in/'
LIST_RESOURCE = 'api/unknown'
SINGLE_RESOURCE = 'api/unknown/2'
SINGLE_RESOURCE_NOT_FOUND = 'api/unknown/23'
ONE_YEAR = 1
COLOR_STARTS = '#'

@allure.suite('Проверка запросов данных ресурсов')
@allure.title('Проверяем получение списка ресурсов')
def test_list_resource():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + LIST_RESOURCE}'):
        response = httpx.get(BASE_URL + LIST_RESOURCE)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    data = response.json()['data']
    for item in data:
        with allure.step('Проверяем элемент из списка'):
            validate(item, RESOURCE_DATA_SCHEMA)
            # assert item["year"].endswith(data["id"] - ONE_YEAR)
            with allure.step('Проверяем начало цвета'):
                assert item["color"].startswith(COLOR_STARTS)

@allure.suite('Проверка запросов данных ресурса')
@allure.title('Проверяем получение данных ресурса')
def test_single_resource():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + SINGLE_RESOURCE}'):
        response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    data = response.json()['data']
    # assert data["year"].endswith(1)
    with allure.step('Проверяем начало цвета'):
        assert data["color"].startswith(COLOR_STARTS)

@allure.suite('Проверка запроса отсутствующего ресурса')
@allure.title('Проверяем получение отсутствующего ресурса')
def test_resource_not_found():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + SINGLE_RESOURCE_NOT_FOUND}'):
        response = httpx.get(BASE_URL + SINGLE_RESOURCE_NOT_FOUND)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 404
