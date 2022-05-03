from crypt import methods
from flask import Blueprint

tienda = Blueprint('tienda',__name__, template_folder='templates')

@tienda.route("/", methods=["GET"])
def index() -> str:
    return "Welcome Home :)"

#-------------------------------CLIENTES------------------------------------------------

cliente = Blueprint('cliente',__name__, template_folder='templates')

@cliente.route("/cliente", methods=["GET"])
def index() -> str:
    return "Enjoy it :)"
