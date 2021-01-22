
import json
import random

HSP_JSON = {"uf": [
    "MATO GROSSO",
    "DISTRITO FEDERAL",
    "MINAS GERAIS",
    "ALAGOAS",
    "PARAIBA",
    "MARANHAO",
    "AMAPA",
    "PERNANBUCO",
    "RORAIMA",
    "CEARA",
    "PARANA",
    "RONDONIA",
    "ACRE",
    "RIO GRANDE DO NORTE",
    "RIO DE JANEIRO",
    "SERGIPE",
    "PIAUI",
    "SANTA CATARINA",
    "SAO PAULO",
    "GOIAS",
    "AMAZONAS",
    "MATO GROSSO DO SUL",
    "BAHIA",
    "TOCANTINS",
    "ESPIRITO SANTO",
    "RIO GRANDE DO SUL",
    "PARA"
]}


def test_get_all_cities_in_database(client):

    response = client.get('/hsp')

    hsp_result =  json.loads(response.data)
    remove_spaces = map(lambda city: city.upper().replace(' ', '').replace('-', ' '), hsp_result['uf'])
    
    assert 'uf' in hsp_result
    assert sorted(remove_spaces) == sorted(HSP_JSON['uf'])


def test_get_one_city_in_database(client):

    random_city = HSP_JSON['uf'][random.randint(0, len(HSP_JSON['uf']) -1)].title().replace(' ', '-')
    response = client.get(f'/hsp/{random_city}')

    hsp_result = json.loads(response.data)

    assert random_city.lower() in hsp_result['uf']
