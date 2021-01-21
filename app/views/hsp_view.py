from app.services.hsp_service import get_uf_or_all
from flask import request
from flask_restful import Resource


class HspUf(Resource):

    def get(self, **kwargs):
        try:
            uf = kwargs.get("uf")
            response = get_uf_or_all(uf=uf)

        except:
            response = get_uf_or_all()

        return response
