from flask import json
import random

def generate_fiels(max):
    return (''.join([
        random.choice("abcdefghijqlimnopkrstuvxwyz")
        for _ in range(max)
        ]) + '@gmail.com', 
        ''.join([random.choice('abcdefghijqlimnopkrstuvxwyz') for _ in range(max)
        ]),
        ''.join([random.choice('1234567890') for _ in range(max)
        ])
    )


def new_lead_json():
    """retorna um json do novo lead"""
    email, name, phone = generate_fiels(10)
    return {
        "name": '[test]' + name,
        "email": email,
        "phone": int(phone),
        "hsp_id": 1,
        "month_energy": 1,
        "month_value": 120
    }

##name, email, phone
def test_create_new_lead(client):
    """cria novo lead e verifica o retorno do post e o status"""

    new_lead = new_lead_json()

    response = client.post('/lead', json=new_lead)

    data = json.loads(response.data)
    status = response.status_code

    expected = {"data": new_lead}
    assert data == expected
    assert status == 201
