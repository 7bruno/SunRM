from http import HTTPStatus

from flask import current_app

from ..models import Lead, Message
from ..schema import lead_schema, message_schema, simulations_schema
from .http_service import build_api_response


def create_message(data):

    try:

        message = Message(
            classification=data['classification'],
            message=data['message'],
            lead_id=data['lead_id'],
            seller_id=data['seller_id']
        )

        session = current_app.db.session
        session.add(message)
        session.commit()

        return build_api_response(HTTPStatus.CREATED, message_schema.dump(message))

    except Exception as error:
        print(error)
        return build_api_response(HTTPStatus.BAD_REQUEST)


def get_message(message_id):

    try:

        message = Message.query.get_or_404(message_id)
        message_schema_rs = message_schema.dump(message)

        return build_api_response(HTTPStatus.OK, message_schema_rs)

    except Exception as error:
        print(error)
        return build_api_response(HTTPStatus.BAD_REQUEST)
