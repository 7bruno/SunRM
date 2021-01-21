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
    id_message_create = last_message_id

    assert sorted(data_result.keys()) == sorted(data_expected.keys())
    assert sorted([str(i) for i in data_result.values()]) == sorted(
        [str(i) for i in data_expected.values()])


def test_dict_of_get_lead_and_message_with_status_200(client):
    """pega o lead e as messagens e verifica o status"""
    response = client.get(f'/message/{1}')

    status_result = response.status_code
    data_result = json.loads(response.data)

    status_expected = 200
    assert status_result == status_expected

    lead_result = data_result['lead'].copy()
    message_result = data_result['message'].copy()

    print(execute_sql_comand_in_database(
        f"""SELECT id, energy_id, phone, name, email FROM lead WHERE lead.id = {1}"""
    )[0])

    id, energy_id, phone, name, email = execute_sql_comand_in_database(
        f"""SELECT id, energy_id, phone, name, email FROM lead WHERE lead.id = {1}"""
    )[0]
    id, seller_id, lead_id, message, classification = execute_sql_comand_in_database(
        f"""SELECT id, seller_id, lead_id, message, classification FROM message WHERE message.lead_id = {1}"""
    )[0]

    lead_expected = {
        'id': id,
        'energy_id': energy_id,
        'phone': phone,
        'name': name,
        'email': email
    }

    message_expected = {
        'id': id,
        'seller_id': seller_id,
        'lead_id': lead_id,
        'message': message,
        'classification': classification
    }

    assert sorted(lead_result.keys()) == sorted(lead_expected.keys())
    assert sorted([str(i) for i in lead_result.values()]) == sorted(
        [str(i) for i in lead_expected.values()])

    assert sorted(message_result.keys()) == sorted(message_expected.keys())
    assert sorted([str(i) for i in message_result.values()]) == sorted(
        [str(i) for i in message_expected.values()])

#>       assert sorted([str(i) for i in lead_result.values()]) == sorted(
#            [str(i) for i in lead_expected.values()])
#E       AssertionError: assert ['1', '1', '40028942244r3', 'christophe4rr', 'christophe4rr@exemple.com'] == ['1', '2', '40028942244r3', 'christophe4rr', 'christophe4rr@exemple.com']
#E         At index 1 diff: '1' != '2'
#E         Full diff:
#E         - ['1', '2', '40028942244r3', 'christophe4rr', 'christophe4rr@exemple.com']
#E         ?        ^
#E         + ['1', '1', '40028942244r3', 'christophe4rr', 'christophe4rr@exemple.com']
#E         ?        ^

#tests/views/test_message_view.py:86: AssertionError
