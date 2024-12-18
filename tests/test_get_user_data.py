import httpx
from jsonschema import validate
from core.contracts import USER_DATA_SCHEMA

BASE_URL = 'https://reqres.in/'
LIST_USERS = 'api/users?page=2'
SINGLE_USER = 'api/users/2'
SINGLE_USER_NOT_FOUND = 'api/users/23'
EMAIL_ENDS = '@reqres.in'
AVATAR_ENDS = '-image.jpg'

def test_list_users():
    # response = httpx.get("https://reqres.in/api/users?page=2")
    response = httpx.get(BASE_URL + LIST_USERS)
    assert response.status_code == 200
    data = response.json()['data']
    # validate(data, USER_DATA_SCHEMA)
    for item in data:
        validate(item, USER_DATA_SCHEMA)
        assert item["email"].endswith(EMAIL_ENDS)
        # assert str(item["id"]) in item["avatar"]
        assert item["avatar"].endswith(str(item["id"]) + AVATAR_ENDS)

    # print(response)
    # print(response.text)
    # print(response.json()['data'])

def test_single_user():
    response = httpx.get(BASE_URL + SINGLE_USER)
    assert response.status_code == 200
    data = response.json()['data']

    assert data["email"].endswith(EMAIL_ENDS)
    assert data["avatar"].endswith(str(data["id"]) + AVATAR_ENDS)

def test_user_not_found():
    response = httpx.get(BASE_URL + SINGLE_USER_NOT_FOUND)
    assert response.status_code == 404

