import jwt


def encode_password(data):
    try:
        criptography = jwt.encode(
            {'email': data['email']}, data['password'], algorithm="HS256")

    except Exception as error:
        print(error)
        return None

    return criptography.decode("utf-8")
