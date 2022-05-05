from ..database.Postgresql import Postgres
from datetime import date

class User():

    __nombre           = str
    __apellidos        = str
    __fecha_nacimiento = date


    def __init__(self, nombre, apellidos, fecha_nacimiento):
        print("Nueva usuario")
        self.__nombre           = nombre
        self.__apellidos        = apellidos
        self.__fecha_nacimiento = fecha_nacimiento


    def actualizar_datos(self, nombre, apellidos, fecha_nacimiento) -> str:
        self.__nombre           = nombre
        self.__apellidos        = apellidos
        self.__fecha_nacimiento = fecha_nacimiento
        return 'Datos actualizados'


    def guardar(self) -> str:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        connection.execute('INSERT INTO "Usuarios" ("nombre", "fecha_nacimiento", "apellidos") VALUES (%s, %t, %s)', 
            (self.__nombre, self.__fecha_nacimiento, self.__apellidos)
        )
        connection.commit()
        postgres_repository.close_connection()
        return 'Usuario guardado'



    @staticmethod
    def obtener_usuarios() -> dict:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        data = connection.execute('SELECT * FROM "Usuarios"').fetchall()
        postgres_repository.close_connection()
    
        response = {}
        index = 1
        for usuario in data:
            response[str(index)] = { 'id' : usuario[0], 'nombre' : usuario[1], 'fecha_nacimiento' : usuario[2], 'apellidos' : usuario[3] }
            index += 1    
        return response
