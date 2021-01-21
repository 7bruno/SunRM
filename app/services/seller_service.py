from datetime import timedelta
from http import HTTPStatus

from app.models import Seller
from app.services.encode_service import encode_password
from flask import current_app
from flask_jwt_extended import create_access_token, create_refresh_token

from .http_service import build_api_response


def login_seller(data):
    try:

        encoded_password = encode_password(data)
        seller = Seller.query.filter_by(
            email=data['email'], password=encoded_password).first()

        acess_token = create_access_token(
            identity=seller.id, expires_delta=timedelta(days=1))
        refresh_token = create_refresh_token(
            identity=seller.id, expires_delta=timedelta(days=1))

        if not seller:
            return build_api_response(HTTPStatus.NOT_FOUND)

        return build_api_response(
            HTTPStatus.OK, {
                'refresh_token': refresh_token,
                'auth_token': acess_token,

                'user': {
                    'id': seller.id,
                    'name': seller.name,
                    'email': seller.email
                }

            }
        )

    except Exception as error:
        print(error)
        return build_api_response(HTTPStatus.BAD_REQUEST)


def create_seller(data):

    try:

        encoded_password = encode_password(data)
        seller = Seller(
            name=data['name'],
            email=data['email'],
            password=encoded_password
        )

        acess_token = create_access_token(
            identity=seller.id, expires_delta=timedelta(days=1))

        session = current_app.db.session
        session.add(seller)
        session.commit()

        return build_api_response(
            HTTPStatus.CREATED, {
                'auth_token': acess_token,

                'user': {
                    'id': seller.id,
                    'name': seller.name,
                    'email': seller.email
                }
            }
        )

    except Exception as error:
        print(error)
        return build_api_response(HTTPStatus.BAD_REQUEST)
