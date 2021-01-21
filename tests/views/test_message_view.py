from flask import json
from tests.database_connection import execute_sql_comand_in_database


def new_message_json():
    """retorna o json com as informações da nova menssagem"""

    return {
        "lead_id": "1",
        "seller_id": "1",
        "classification": "5",
        "message": "O lead quer uma proposta formalizada por email."
    }


new_message = new_message_json()


def test_dict_create_message_with_status_201(client):
    """cria uma nova messagem e verifica as informações do json sem o id"""

    response = client.post('/message', json=new_message)

    status_result = response.status_code
    data_result = json.loads(response.data)

    status_expected = 201
    assert status_result == status_expected

    data_expected = new_message.copy()

    assert int(data_result['id']) > 0
    assert type(data_result['id']) is int

    last_message_id = execute_sql_comand_in_database(
        """SELECT id FROM message ORDER BY ID DESC LIMIT 1""")[0][0]

    data_expected.update({'id': last_message_id})

    assert sorted(data_result.keys()) == sorted(data_expected.keys())
    assert sorted([str(i) for i in data_result.values()]) == sorted(
        [str(i) for i in data_expected.values()])


def test_dict_of_get_lead_and_message_with_status_200(client):
    """pega o lead e as messagens e verifica o status"""

    message_id = execute_sql_comand_in_database(
        """SELECT id FROM message ORDER BY ID DESC LIMIT 1""")[0][0]

    print(message_id)
    response = client.get(f'/message/{message_id}')

    status_result = response.status_code
    data_result = json.loads(response.data)

    status_expected = 200
    assert status_result == status_expected

    lead_result = data_result['lead'].copy()
    message_result = data_result['message'].copy()

    print(lead_result, message_result)

    id, energy_id, phone, name, email = execute_sql_comand_in_database(
        f"""SELECT id, energy_id, phone, name, email FROM lead WHERE lead.id = {lead_result['id']}"""
    )[0]

    lead_expected = {
        'id': id,
        'energy_id': energy_id,
        'phone': phone,
        'name': name,
        'email': email
    }

    id, seller_id, lead_id, message, classification = execute_sql_comand_in_database(
        f"""SELECT id, seller_id, lead_id, message, classification 
        FROM message WHERE message.lead_id = {message_result['lead_id']}"""
    )[0]

    message_expected = {
        'id': id,
        'seller_id': seller_id,
        'lead_id': lead_id,
        'message': message,
        'classification': classification
    }

    print(lead_expected, message_expected)


    assert sorted(lead_result.keys()) == sorted(lead_expected.keys())
    assert sorted([str(i) for i in lead_result.values()]) == sorted(
        [str(i) for i in lead_expected.values()])

    assert sorted(message_result.keys()) == sorted(message_expected.keys())
    assert sorted([str(i) for i in message_result.values()]) == sorted(
        [str(i) for i in message_expected.values()])
