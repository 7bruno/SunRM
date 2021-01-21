from . import db


class Message(db.Model):
    __tablename__ = "message"

    id = db.Column(db.Integer, primary_key=True)
    classification = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String, nullable=False)

    lead_id = db.Column(db.Integer, db.ForeignKey(
        'lead.id', onupdate='CASCADE', ondelete='CASCADE'))
    seller_id = db.Column(db.Integer, db.ForeignKey(
        'seller.id', onupdate='CASCADE', ondelete='CASCADE'))
