from .database.Postgresql import Postgres as __Postgresql
from flask import Blueprint

#-------------------------------TIENDA------------------------------------------------

tienda = Blueprint('tienda',__name__, template_folder='templates')

@tienda.route("/", methods=["GET"])
def index() -> str:
    __postgres_repository = __Postgresql()
    __postgres_repository.create_connection()
    connection = __postgres_repository.get_connection()
    cur = str(connection.execute("SELECT now()").fetchone())
    return cur

#-------------------------------CLIENTES------------------------------------------------

cliente = Blueprint('cliente',__name__, template_folder='templates')

@cliente.route("/cliente", methods=["GET"])
def index() -> str:
    return "Enjoy it :)"
