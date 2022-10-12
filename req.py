import json

import requests

base_url = 'https://petstore.swagger.io/v2'


def get_user_by_user_name(username):
    res = requests.get(f'{base_url}/user/{username}',
                       headers={'accept': 'application/json'})
    print(res.status_code)
    print(res.json())


get_user_by_user_name('user1')


def finds_pets_by_status(status):
    res = requests.get(f'{base_url}/pet/findByStatus?status={status}',
                       headers={'accept': 'application/json'})

    print(res.status_code)
    return res.json()


# available_pets = finds_pets_by_status('available')
# print(available_pets)
# pending_pets = finds_pets_by_status('pending')
# print(pending_pets)
sold_pets = finds_pets_by_status('sold')
print(sold_pets)


new_pet = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "мультяшный герой"
  },
  "name": "крокодил Гена",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}


def add_new_pet(body):
    res = requests.post(f'{base_url}/pet',
                        headers={'accept': 'application/json',
                                 'Content-Type': 'application/json'},
                        data=json.dumps(body).encode('utf-8'))
    print(res.status_code)
    return res.json()


added_pet = add_new_pet(new_pet)
print(added_pet)
petid = added_pet['id']


def find_pet_by_id(pet_id):
    res = requests.get(f'{base_url}/pet/{pet_id}',
                       headers={'accept': 'application/json'})
    print(res.status_code)
    print(res.json())


find_pet_by_id(petid)


existing_pet = {
  "id": petid,
  "category": {
    "id": 0,
    "name": "Котейка"
  },
  "name": "кошка",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}


def update_existing_pet(body):
    res = requests.put(f'{base_url}/pet',
                       headers={'accept': 'application/json',
                                'Content-Type': 'application/json'},
                       data=json.dumps(body).encode('utf-8'))
    print(res.status_code)
    print(res.json())


update_existing_pet(existing_pet)


def delete_pet(pet_id):
    res = requests.delete(f'{base_url}/pet/{pet_id}',
                          headers={'accept': 'application/json'})
    print(res.status_code)


delete_pet(petid)
find_pet_by_id(petid)
