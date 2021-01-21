from http import HTTPStatus


def build_api_response(http_status, schema=None):
    return build_response_message(http_status, schema), http_status


def build_response_message(http_status, schema):
    messages = {
        HTTPStatus.BAD_REQUEST: 'Bad request',
        HTTPStatus.NOT_FOUND: 'Not found',
        HTTPStatus.CREATED: schema,
        HTTPStatus.OK: schema
    }

    request = messages[http_status]

    return request
