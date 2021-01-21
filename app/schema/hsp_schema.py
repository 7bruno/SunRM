
from ..models import Hsp
from . import ma


class HspSchema(ma.SQLAlchemySchema):
    class Meta:

        model = Hsp

    id = ma.auto_field()
    city = ma.auto_field()
    uf = ma.auto_field()


hsp_schema = HspSchema()
hsps_schema = HspSchema(many=True)
