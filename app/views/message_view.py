from http import HTTPStatus

from app.services.message_service import create_message, get_message
from flask import request
from flask_restful import Resource


class Message(Resource):

    def get(self, message_id):

        request = get_message(message_id)
        return request

    def post(self):
        data = request.get_json()

        response = create_message(data)
        return response
