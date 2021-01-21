from app.services.decode_service import decode_password
from app.services.encode_service import encode_password


def test_should_return_a_decoded_data():
    data = {
        'name': '[TEST] Example Name',
        'email': 'example_email@gmail.com',
        'password': '1234'
    }
    encoded_data = encode_password(data)
    key = data['password']

    result = decode_password(encoded_data, key).get('email')
    expected = data['email']

    assert result == expected
