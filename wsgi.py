from os import environ

from app import create_app

application = create_app(environ.get('FLASK_ENV'))

if __name__ == '__main__':
    application.run()
