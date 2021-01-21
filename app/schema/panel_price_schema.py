from ..models import PanelPrice
from . import ma


class PanelPriceSchema(ma.SQLAlchemySchema):

    class Meta:

        model = PanelPrice

    id = ma.auto_field()
    model = ma.auto_field()
    brand = ma.auto_field()
    power = ma.auto_field()
    price = ma.auto_field()


panel_price_schema = PanelPriceSchema()
panels_prices_schema = PanelPriceSchema(many=True)
