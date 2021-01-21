from marshmallow import fields

from ..models import Simulation
from . import ma


class SimulationSchema(ma.SQLAlchemySchema):

    class Meta:

        model = Simulation

    system_cost = fields.Float()
    energy_cost = fields.Float()
    worker_cost = fields.Float()
    project_cost = fields.Float()
    eletric_materials_cost = fields.Float()
    maintanance_cost = fields.Float()
    total_system_cost = fields.Float()
    roi_years = fields.Float()
    panel_quantity = fields.Float()

    lead_id = ma.auto_field()
    panel_id = ma.auto_field()
    inversor_id = ma.auto_field()


simulation_schema = SimulationSchema()
simulations_schema = SimulationSchema(many=True)
