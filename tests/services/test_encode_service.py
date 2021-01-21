from app.services.encode_service import encode_password


def test_should_return_a_encoded_password():
    example_data = {
        'email': 'example@example.com',
        'password': '12345'
    }
    expected = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImV4YW1wbGVAZXhhbXBsZS5jb20ifQ.mNwo9wLtoMSolkjpMLwMNdVw8uVNzWrdTAR_sQ_me0U'
    encoded_password = encode_password(example_data)

    assert expected == encoded_password, 'The password should be encoded'
