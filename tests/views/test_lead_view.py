from flask import json
import random

def generate_fiels(max):
    return (''.join([
        random.choice("abcdefghijqlimnopkrstuvxwyz")
        for _ in range(max)
        ]) + '@gmail.com', 
        ''.join([random.choice('abcdefghijqlimnopkrstuvxwyz') for _ in range(max)
        ]),
        ''.join([random.choice(1234567890) for _ in range(max)
        ])
    )


def new_lead_json():
    """retorna um json do novo lead"""

    return {
        "name": "[TEST] Example Name",
        "email": "example_email@gmail.com",
        "phone": 00000000,
        "hsp_id": 1,
        "energy_id": 1,
    }

##name, email, phone
def test_create_new_lead(client):
    """cria novo lead e verifica o retorno do post e o status"""

    new_lead = new_lead_json()

    response = client.post('/lead', json=new_lead)

    data = json.loads(response.data)
    status = response.status_code

    expected = {"data": new_lead}
    print(generate_fiels)
    
    assert data == expected
    assert status == 201
