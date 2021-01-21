from marshmallow import fields

from ..models import Lead
from . import ma
from .simulation_schema import SimulationSchema


class LeadSchema(ma.SQLAlchemySchema):

    class Meta:

        model = Lead
        include_relationships = True
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    phone = ma.auto_field()

    energy_id = ma.auto_field()
    # simulations = fields.Nested(SimulationSchema(many=True, only=('project_cost',)))
    simulations = fields.Nested(SimulationSchema(many=True))


lead_schema = LeadSchema()
leads_schema = LeadSchema(many=True)
