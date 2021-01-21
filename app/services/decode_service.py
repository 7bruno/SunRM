import jwt


def decode_password(encoded_data, key):
    decoded_data = jwt.decode(encoded_data, key, algorithms=["HS256"])

    return decoded_data
