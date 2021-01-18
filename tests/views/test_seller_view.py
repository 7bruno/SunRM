import ast
import random
from flask import json
from flask_jwt_extended import JWTManager
from app.services.decode_service import decode_password
from app.services.encode_service import encode_password

def email_generator(max):
    return ''.join([random.choice("abcde") for _ in range(max)]) + '@gmail.com'


random_email = email_generator(20)


def new_seller_json():
    """retorna um json com as informações no novo seller"""

    return {
        'name': "Christopher",
        'email': random_email,
        'password': "121314"
    }


def test_create_seller(client):
    """cria um novo seller e compara o status"""
    json_data = new_seller_json()
    response = client.post('/register', json=json_data)
    token = json.loads(response.data)['data'].get('auth_token')
    result = json.loads(response.data)['data'].get('user')['email']
    expected = json_data['email']

    assert expected == result 
    assert response.status_code == 201


def test_login_seller(client):
    """loga com o novo seller criado e compara o status"""
    json_data = new_seller_json()
    response = client.post('/login', json=json_data)
    result = json.loads(response.data)['data'].get('auth_token')
    expected = True

    assert expected == result, 'Length should be bigger than 0'
    assert response.status_code == 200
    
