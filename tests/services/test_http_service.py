from http import HTTPStatus

from app.services.http_service import build_api_response


def test_should_be_a_bad_request():

    message, status = build_api_response(HTTPStatus.BAD_REQUEST)

    assert message == 'Bad request'
    assert status == HTTPStatus.BAD_REQUEST


def test_should_be_a_not_found():

    message, status = build_api_response(HTTPStatus.NOT_FOUND)

    assert message == 'Not found'
    assert status == HTTPStatus.NOT_FOUND


def test_should_be_create_with_the_message():

    send_data = {"test": 'this is a test message'}
    message, status = build_api_response(HTTPStatus.CREATED, send_data)

    assert message == send_data
    assert status == HTTPStatus.CREATED


def test_should_be_ok_with_the_message():

    send_data = {"test": 'this is a test message'}
    message, status = build_api_response(HTTPStatus.OK,  send_data)

    assert message == send_data
    assert status == HTTPStatus.OK


def test_should_be_create_with_none_message():

    message, status = build_api_response(HTTPStatus.CREATED)

    assert message == None
    assert status == HTTPStatus.CREATED


def test_should_be_ok_with_none_message():

    message, status = build_api_response(HTTPStatus.OK)

    assert message == None
    assert status == HTTPStatus.OK
