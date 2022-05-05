from pathlib import Path
from .database.Postgresql import Postgres as __Postgresql
from flask import Blueprint, render_template

#-------------------------------DB-STATE------------------------------------------------
dbstate = Blueprint('dbstate',__name__, template_folder=Path(__file__).parents[1].name +'templates')


@dbstate.route("/db-state", methods=["GET"])
def check_connection_db() -> str:
    __postgres_repository = __Postgresql()
    __postgres_repository.create_connection()
    connection = __postgres_repository.get_connection()
    cur = str(connection.execute("SELECT now()").fetchone())
    return cur

#-------------------------------INICIO------------------------------------------------
inicio = Blueprint('inicio',__name__, template_folder='templates')


@inicio.route("/", methods=["GET"])
def index() -> str:
    return render_template('index.html')
