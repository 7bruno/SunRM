from flask import json


def new_lead_json():
    """retorna um json do novo lead"""

    return {
        "name": "[TEST] Example Name",
        "email": "example_email@gmail.com",
        "phone": 00000000,
        "hsp_id": 1,
        "energy_id": 1,
    }


def test_create_new_lead(client):
    """cria novo lead e verifica o retorno do post e o status"""

    new_lead = new_lead_json()

    # response = client.post('/lead', json=new_lead)

    # data = json.loads(response.data)
    # status = response.status_code

    # expected = {"data": new_lead}

    # assert data == expected
    # assert status == 201
