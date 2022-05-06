from ..database.Postgresql import Postgres
from datetime import date

class User():

    __id               = int
    __nombre           = str
    __apellidos        = str
    __fecha_nacimiento = date


    def __init__(self, nombre : str, apellidos : str, fecha_nacimiento : date):
        print("Nuevo usuario")
        self.__id               = 0
        self.__nombre           = nombre
        self.__apellidos        = apellidos
        self.__fecha_nacimiento = fecha_nacimiento


    def actualizar(self, nombre, apellidos, fecha_nacimiento) -> str:
        if self.__id <= 0 :
            return 'Error: Usuario no registrado'
        
        self.__nombre           = nombre
        self.__apellidos        = apellidos
        self.__fecha_nacimiento = fecha_nacimiento

        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        connection.execute('UPDATE "Usuarios" SET "nombre" = %s, "fecha_nacimiento" = %t, "apellidos" = %s WHERE id = %s', 
            (self.__nombre, self.__fecha_nacimiento, self.__apellidos, str(self.__id))
        )
        connection.commit()
        postgres_repository.close_connection()
        
        return 'Usuario actualizado'


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
        data = connection.execute('SELECT id, nombre, apellidos, fecha_nacimiento FROM "Usuarios"').fetchall()
        postgres_repository.close_connection()
    
        response = {}
        index = 1
        for usuario in data:
            response[str(index)] = { 'id' : usuario[0], 'nombre' : usuario[1], 'fecha_nacimiento' : usuario[2], 'apellidos' : usuario[3] }
            index += 1    
        return response


    @staticmethod
    def buscar(user_id: int) -> object:
        postgres_repository = Postgres()
        postgres_repository.create_connection()
        connection = postgres_repository.get_connection()
        data = connection.execute('SELECT id, nombre, apellidos, fecha_nacimiento FROM "Usuarios" WHERE id = %s', (user_id,)).fetchone()
        postgres_repository.close_connection()

        user = User(data[1], data[2], data[3])
        user.__id = data[0]
        return user


    def to_json_dict(self) -> dict:
        return {'id' : self.__id, 'nombre' : self.__nombre, 'apellidos' : self.__apellidos, 'fecha_nacimiento' : self.__fecha_nacimiento}
