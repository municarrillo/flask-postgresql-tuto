class Tienda():

    __connection = None

    def __init__(self, connection):
        print("Nueva tienda")
        self.__connection = connection

    def is_connection_available(self):
        if self.__connection is not None:
            return True
        return False
