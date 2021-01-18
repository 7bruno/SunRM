from app.models import Hsp, Energy_data, Panel_price, energy_data_model


def panel_set_costs(pow_pico, pow_panel, price_panel):
    pow_pico = pow_pico * 1000
    panel_set_price = ((pow_pico//pow_panel) + 1) * price_panel

    return panel_set_price


def inversor_selector(inversor_list):
    def sort_inversors(e):
        return e.price

    available_inversors = list(
        filter(lambda inversor: inversor.power/0.8 >= ppico, inversor_list))
    available_inversors.sort(key=sort_inversors)
    return available_inversors[0]


def panel_selector(panel_list, pow_pico):

    def sort_panel(e):
        return panel_set_costs(pow_pico, e.power, e.price)

    panel_list.sort(key=sort_panel)
    selected_panel = panel_list[0]
    selected_panel_quantity = pow_pico//selected_panel.power + 1

    return {
        "panel": selected_panel,
        "quantity": selected_panel_quantity
    }


def roi_calc(energy_data, inversor_list, panel_list, hsp):
    power_pico = installed_power(hsp, energy_data)*1000
    inversor = inversor_selector(inversor_list, power_pico)
    panel = panel_selector(panel_list, power_pico)

    energy_cost = energy_data.month_value*12*25
    system_cost = inversor.price + panel["panel"].price * panel["quantity"]
    worker_cost = system_cost*0.2  # mão de obra custa em torno de 20% do equipamento
    # criar o projeto fica em média 40% do custo do equipamento
    project_cost = system_cost*0.4
    # materiais elétricos são estimados como 10% dos equipamentos
    eletric_materials_cost = system_cost*0.1
    # manutenção do sistema custa 0.5% ao ano, em 25 anos o custo fica em 12.5%
    maintenance_cost = system_cost * 0.125

    total_system_cost = system_cost + worker_cost + \
        project_cost + eletric_materials_cost + maintenance_cost

    roi_years = (total_system_cost/energy_data.month_value) / 12

    return {
        "inversor": inversor,
        "panel": panel,
        "energy_cost": energy_cost,
        "system_cost": system_cost,
        "worker_cost": worker_cost,
        "project_cost": project_cost,
        "eletric_materials_cost": eletric_materials_cost,
        "maintanance_cost": maintenance_cost,
        "total_system_cost": total_system_cost,
        "roi_years": roi_years
    }
