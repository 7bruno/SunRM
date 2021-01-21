from . import db


class HspLead(db.Model):
    __tablename__ = "hsp_lead"

    id = db.Column(db.Integer, primary_key=True)

    hsp_id = db.Column(db.Integer, db.ForeignKey('hsp.id'))
    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'))
