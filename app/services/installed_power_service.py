from app.models import EnergyData, Hsp


def installed_power(db_hsp: Hsp, energy_data: EnergyData):

    hsp = db_hsp.md_anual/1000
    diary_energy = energy_data.month_energy/30
    ppico = diary_energy/hsp
    eficience = 0.8
    ppico_real = ppico/eficience

    return ppico_real
