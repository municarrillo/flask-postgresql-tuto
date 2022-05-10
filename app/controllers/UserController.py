from array import array
from app.models.User import User
from pathlib import Path
from flask import Blueprint, render_template, request

usuarios = Blueprint('usuarios',__name__, template_folder=Path(__file__).parents[1].name + 'templates')

@usuarios.route("/usuarios/guardar", methods=["POST"])
def __save_usuario() -> str:
    nombre           = request.get_json()['nombre']
    fecha_nacimiento = request.get_json()['fecha_nacimiento']
    apellidos        = request.get_json()['apellidos']

    nuevo_usuario = User(nombre, apellidos, fecha_nacimiento)
    message = nuevo_usuario.guardar()

    return str('{"message": "%s"}' % message)


@usuarios.route("/usuarios/actualizar", methods=["PUT"])
def __edit_usuario() -> str:
    user_id          = request.get_json()['id']
    nombre           = request.get_json()['nombre']
    fecha_nacimiento = request.get_json()['fecha_nacimiento']
    apellidos        = request.get_json()['apellidos']

    usuario_to_edit = User.buscar(user_id)
    message = usuario_to_edit.actualizar(nombre, apellidos, fecha_nacimiento)

    return str('{"message": "%s"}' % message)


@usuarios.route("/usuarios/mostrar", methods=["GET"])
def __mostrar_usuarios() -> str:
    return render_template('Usuarios.html')


@usuarios.route("/usuarios", methods=["GET"])
def __get_usuarios() -> str:
    resp = User.obtener_usuarios()
    return resp


@usuarios.route("/usuarios/buscar", methods=["GET"])
def __buscar_usuario() -> str:
    user_id = request.args['id']
    resp = User.buscar(user_id)
    return resp.to_json_dict()


@usuarios.route("/usuarios/registrar", methods=["GET"])
def __formulario_registro():
    return render_template('FormRegistrarUsuario.html')


@usuarios.route("/usuarios/editar", methods=["GET"])
def __formulario_edicion():
    return render_template('FormEditarUsuario.html')
