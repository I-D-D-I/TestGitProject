import httpx
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SCHEMA

BASE_URL = 'https://reqres.in/'
LIST_RESOURCE = 'api/unknown'
SINGLE_RESOURCE = 'api/unknown/2'
SINGLE_RESOURCE_NOT_FOUND = 'api/unknown/23'
ONE_YEAR = 1
COLOR_STARTS = '#'

def test_list_resource():
    response = httpx.get(BASE_URL + LIST_RESOURCE)
    assert response.status_code == 200
    data = response.json()['data']
    for item in data:
        validate(item, RESOURCE_DATA_SCHEMA)
        # assert item["year"].endswith(data["id"] - ONE_YEAR)
        assert item["color"].startswith(COLOR_STARTS)

def test_single_resource():
    response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    assert response.status_code == 200
    data = response.json()['data']
    # assert data["year"].endswith(1)
    assert data["color"].startswith(COLOR_STARTS)

def test_resource_not_found():
    response = httpx.get(BASE_URL + SINGLE_RESOURCE_NOT_FOUND)
    assert response.status_code == 404
