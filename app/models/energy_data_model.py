from . import db


class EnergyData(db.Model):
    __tablename__ = "energy_data"

    id = db.Column(db.Integer, primary_key=True)
    month_energy = db.Column(db.Numeric, nullable=False)
    month_value = db.Column(db.Numeric, nullable=False)
    leads = db.relationship('Lead', uselist=False)
