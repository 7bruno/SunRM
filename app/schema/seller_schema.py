from marshmallow import fields

from ..models import Seller
from . import ma


class SellerSchema(ma.SQLAlchemySchema):
    class Meta:

        model = Seller

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()
    lead_id = ma.auto_field()


seller_schema = SellerSchema()
sellers_schema = SellerSchema(many=True)
