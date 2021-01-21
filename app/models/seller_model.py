from . import db, ma


class Seller(db.Model):
    __tablename__ = "seller"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    lead_id = db.relationship('Lead', secondary='message')


class SellerSchema(ma.SQLAlchemySchema):
    class Meta:

        fields = ('id', 'name', 'email', 'password', 'lead_id')


seller_schema = SellerSchema()
sellers_schema = SellerSchema(many=True)
