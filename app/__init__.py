from .database.Postgresql import Postgres as __Postgresql
from .routes import tienda as __tienda, cliente as __cliente
from flask import Flask

# Variables innacesibles al importar este modulo
__postgres_repository = __Postgresql()
__postgres_connection = None
__app                 = None

def create_connections():
    __postgres_connection = __postgres_repository.create_connection()

def close_connections():
    __postgres_connection = None
    __postgres_repository.close_connection()

def get_flask_server() -> Flask:
    __app = Flask(__name__)
    __app.config.from_pyfile("config/flask_config.cfg")
    __app.register_blueprint(__tienda)
    __app.register_blueprint(__cliente)
    return __app
