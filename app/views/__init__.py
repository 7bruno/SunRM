from flask import Flask
from flask_restful import Api

from .hsp_view import HspUf
from .lead_view import LeadView
from .message_view import Message
from .seller_view import SellerLogin, SellerRegister


def configure(app: Flask):

    api = Api(app)
    api.add_resource(SellerRegister, '/register')
    api.add_resource(SellerLogin, '/login')
    api.add_resource(Message, '/message', '/message/<int:message_id>')
    api.add_resource(HspUf, '/hsp', '/hsp/<string:uf>')
    api.add_resource(LeadView, '/lead', '/lead/<int:lead_id>')
