from ..connections.RepositorioPostgres import Postgres

class Tienda():
    __repository = Postgres()
    __connection = any

    def __init__(self):
        self.__connection = self.__repository.get_connection()

    def test_connection(self):
        if (self.__connection is not None):
            print(self.__connection)
            self.__repository.close_conexion()
