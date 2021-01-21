from app.models import EnergyData, Hsp
from app.services.installed_power_service import installed_power


def test_should_be_914():

    hsp_value = Hsp(city='CITY', uf='UF', md_anual=4.556, lon=0, lat=0)
    energy_value = EnergyData(month_energy=100)

    result = installed_power(hsp_value, energy_value)
    expected = 914.5449224465906

    assert result == expected


def test_should_be_1041():

    hsp_value = Hsp(city='CITY', uf='UF', md_anual=4, lon=0, lat=0)
    energy_value = EnergyData(month_energy=100)

    result = installed_power(hsp_value, energy_value)
    expected = 1041.6666666666667

    assert result == expected


def test_should_be_1666():

    hsp_value = Hsp(city='CITY', uf='UF', md_anual=5, lon=0, lat=0)
    energy_value = EnergyData(month_energy=200)

    result = installed_power(hsp_value, energy_value)
    expected = 1666.6666666666665

    assert result == expected


def test_should_be_208():

    hsp_value = Hsp(city='CITY', uf='UF', md_anual=6, lon=0, lat=0)
    energy_value = EnergyData(month_energy=30)

    result = installed_power(hsp_value, energy_value)
    expected = 208.33333333333331

    assert result == expected


def test_should_be_4166():

    hsp_value = Hsp(city='CITY', uf='UF', md_anual=3, lon=0, lat=0)
    energy_value = EnergyData(month_energy=300)

    result = installed_power(hsp_value, energy_value)
    expected = 4166.666666666667

    assert result == expected
