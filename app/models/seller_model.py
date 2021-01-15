from . import db, ma


class Seller(db.Model):
    __tablename__ = "seller"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Seller {self.name}>'


class SellerSchema(ma.SQLAlchemySchema):
    class Meta:

        fields = ('id', 'name', 'email', 'password')

        id = ma.auto_field()
        name = ma.auto_field()
        email = ma.auto_field()
        password = ma.auto_field()


seller_schema = SellerSchema()
sellers_schema = SellerSchema(many=True)