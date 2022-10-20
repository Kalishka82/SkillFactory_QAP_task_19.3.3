import pytest
from faker import Faker
import random
import json
import requests


@pytest.fixture
def fix():
    fake = Faker()
    pet_id = random.randint(1, 999999999999)
    input_pet = {
        "id": pet_id,
        "category": {
            "id": random.randint(1, 999999999999),
            "name": fake.name()
        },
        "name": fake.name(),
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": random.randint(1, 999999999999),
                "name": fake.name()
            }
        ],
        "status": "available"
    }
    header = {'accept': 'application/json', 'Content-Type': 'application/json'}
    return pet_id, input_pet, header


@pytest.fixture()
def yield_fix(fix):
    pet_id, input_pet, header = fix

    requests.post(url='https://petstore.swagger.io/v2/pet',
                  data=json.dumps(input_pet), headers=header)
    print('add pet')

    yield pet_id, input_pet

    res_delete = requests.delete(url=f'https://petstore.swagger.io/v2/pet/{pet_id}',
                                 headers={'accept': 'application/json'})
    print('del pet')
