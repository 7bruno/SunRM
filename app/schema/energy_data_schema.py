from marshmallow import fields

from ..models import EnergyData
from . import ma


class EnergyDataSchema(ma.SQLAlchemySchema):
    class Meta:

        model = EnergyData

    id = ma.auto_field()
    month_energy = ma.auto_field()
    month_value = ma.auto_field()

    leads = fields.Nested('Lead')


energy_data_schema = EnergyDataSchema()
