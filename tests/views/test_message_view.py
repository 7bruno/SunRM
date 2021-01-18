from flask import json


def new_message_json():
    """retorna o json com as informações da nova menssagem"""

    return {
        "lead_id": 1,
        "classification": 5,
        "message": "O lead quer uma proposta formalizada por email."
    }


def test_create_message(client):
    """cria uma nova messagem e verifica as informações do json sem o id"""

    new_message = new_message_json()

    response = client.post('/message', json=new_message)

    status = response.status_code
    data = json.loads(response.data)['data']
    data.pop('id')
    expected = new_message.copy()

    assert status == 201
    assert data == expected
    assert sorted(data.keys()) == sorted(expected.keys())


def test_get_lead_by_message(client):
    """pega o lead e as messagens e verifica o status"""

    new_message = new_message_json()
    response = client.get(f'/message/{1}')
    result = json.loads(response.data)['data'].get('messages')
    especific_message = [message for message in result if message['id'] == 1][0]
    expected = list(filter(lambda message: message.get('lead_id') == especific_message['lead_id'], result))
    
    assert len(result) == len(expected)
    assert response == 200