from app.models.User import User
from pathlib import Path
from flask import Blueprint, render_template, request

usuarios = Blueprint('usuarios',__name__, template_folder=Path(__file__).parents[1].name + 'templates')

@usuarios.route("/usuarios/save", methods=["POST"])
def __save_usuario() -> str:
    nombre           = request.get_json()['nombre']
    fecha_nacimiento = request.get_json()['fecha_nacimiento']
    apellidos        = request.get_json()['apellidos']

    nuevo_usuario = User(nombre, apellidos, fecha_nacimiento)
    message = nuevo_usuario.guardar()

    return str('{"message": "%s"}' % message)


@usuarios.route("/usuarios", methods=["GET"])
def __get_usuarios() -> str:
    resp = User.obtener_usuarios()
    return resp

@usuarios.route("/usuarios/registrar", methods=["GET"])
def __formulario_registro():
    return render_template('FormUsuarios.html')
