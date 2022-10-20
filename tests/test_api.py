import pytest
import json
import requests


def test_add_pet(fix):
    pet_id, input_pet, header = fix
    print(pet_id)

    res_post = requests.post(url='https://petstore.swagger.io/v2/pet',
                             data=json.dumps(input_pet), headers=header)
    # print(res_post.json())
    assert res_post.status_code == 200
    assert res_post.json() == input_pet

    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{pet_id}', headers=header)
    assert res_get.status_code == 200
    # print(res_get.json())
    assert res_get.json() == res_post.json() == input_pet

    res_delete = requests.delete(url=f'https://petstore.swagger.io/v2/pet/{pet_id}',
                                 headers={'accept': 'application/json'})
    assert res_delete.status_code == 200
    # print(res_delete.json())
    assert res_delete.json()['message'] == str(pet_id)

    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{pet_id}',
                           headers={'accept': 'application/json'})
    assert res_get.status_code == 404   # Not Found
    assert res_get.json()['message'] == 'Pet not found'


def test_yield_fix(yield_fix):
    pet_id, input_pet = yield_fix
    print(pet_id)
    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{pet_id}',
                           headers={'accept': 'application/json'})
    assert res_get.status_code == 200
    assert res_get.json() == input_pet
    print('get pet')

