
import json
import random

HSP_JSON = {"uf": [
    "MATO GROSSO",
    "DISTRITO FEDERAL",
    "MINAS GERAIS",
    "ALAGOAS",
    "PARAÍBA",
    "MARANHÃO",
    "AMAPÁ",
    "PERNAMBUCO",
    "RORAIMA",
    "CEARÁ",
    "PARANÁ",
    "RONDÔNIA",
    "ACRE",
    "RIO GRANDE DO NORTE",
    "RIO DE JANEIRO",
    "SERGIPE",
    "PIAUÍ",
    "SANTA CATARINA",
    "SÃO PAULO",
    "GOIÁS",
    "AMAZONAS",
    "MATO GROSSO DO SUL",
    "BAHIA",
    "TOCANTINS",
    "ESPÍRITO SANTO",
    "RIO GRANDE DO SUL",
    "PARÁ"
]}


def test_get_all_cities_in_database(client):

    response = client.get('/hsp')

    hsp_result = json.loads(response.data)

    assert 'uf' in hsp_result
    assert sorted(hsp_result['uf']) == sorted(HSP_JSON['uf'])


def test_get_one_city_in_database(client):

    random_city = HSP_JSON['uf'][random.randint(0, len(HSP_JSON['uf']) -1)]

    response = client.get(f'/hsp/{random_city}')

    hsp_result = json.loads(response.data)

    for city in hsp_result['data']:

        for key in ("id", "uf", "city"):
            assert key in city

        assert city['uf'] == random_city
