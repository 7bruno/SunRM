from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
mg = Migrate()


def configure(app: Flask):
    db.init_app(app)
    mg.init_app(app, db)
    app.db = db

    
from .inverter_price_model import InverterPrice
from .panel_price_model import PanelPrice

from .energy_data_model import EnergyData
from .hsp_model import  Hsp
from .lead_model import Lead
from .seller_model import Seller

from .simulation_model import Simulation
from .message_model import Message
from .hsp_lead_model import HspLead

