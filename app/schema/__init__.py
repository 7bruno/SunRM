from flask import Flask
from flask_marshmallow import Marshmallow

ma = Marshmallow()


def configure(app: Flask):
    ma.init_app(app)


from .inverter_price_schema import inversor_price_schema, inversors_prices_schema
from .panel_price_schema import panel_price_schema, panels_prices_schema

from .energy_data_schema import energy_data_schema
from .hsp_schema import  hsp_schema, hsps_schema
from .lead_schema import lead_schema, leads_schema
from .seller_schema import seller_schema, sellers_schema

from .simulation_schema import simulation_schema, simulations_schema
from .message_schema import message_schema, messages_schema
