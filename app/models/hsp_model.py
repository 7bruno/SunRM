from . import db


class Hsp(db.Model):
    __tablename__ = "hsp"

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), nullable=False)
    uf = db.Column(db.String(120), nullable=False)
    md_anual = db.Column(db.Integer, nullable=False)
    lon = db.Column(db.Numeric, nullable=False)
    lat = db.Column(db.Numeric, nullable=False)

    lead = db.relationship('Lead', secondary='hsp_lead')
