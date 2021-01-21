from ..models import InverterPrice
from . import ma


class InverterPriceSchema(ma.SQLAlchemySchema):

    class Meta:

        model = InverterPrice

    id = ma.auto_field()
    model = ma.auto_field()
    brand = ma.auto_field()
    power = ma.auto_field()
    price = ma.auto_field()


inversor_price_schema = InverterPriceSchema()
inversors_prices_schema = InverterPriceSchema(many=True)
