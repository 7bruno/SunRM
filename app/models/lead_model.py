from . import db


class Lead(db.Model):
    __tablename__ = "lead"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False, unique=True)

    energy_id = db.Column(db.Integer, db.ForeignKey('energy_data.id'))

    simulations = db.relationship('Simulation')
    hsp = db.relationship('Hsp', secondary='hsp_lead')
    seller = db.relationship('Seller', secondary='message')
