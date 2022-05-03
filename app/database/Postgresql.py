# https://www.psycopg.org/psycopg3/docs/basic/usage.html#connection-context
import psycopg
from configparser import ConfigParser
from pathlib import Path


class Postgres():
	""" Connect to the PostgreSQL database server """
	__connection = None
	__path_config_file = Path(__file__).parents[1].name + '/config/db_config.ini' # Ruta de archivo de configuracion config.ini
	__params = None

	def __init__(self):
		try:
			self.__params = self.__config()
		except Exception as error:
			print(error)


	def __config(self, section='postgresql'):
		"""Read credentias from config file"""
		parser = ConfigParser()
		parser.read(self.__path_config_file)
	
		# get section, default to postgresql
		db = {}
		if parser.has_section(section):
			params = parser.items(section)
			for param in params:
				db[param[0]] = param[1]
		else:
			raise Exception('Section {0} not found in the {1} file'.format(section, self.__path_config_file))
	
		return db


	def create_connection(self):
		"""Create connection to PostgreSQL"""
		if self.__params is None:
			print("ERROR: No config file found: File", self.__path_config_file)
			return None

		try:
			if self.__connection is None:
				self.__connection = psycopg.connect(**self.__params)
				print("Success: Connected to PostgreSQL")
				print(self.__connection)
		except (Exception, psycopg.DatabaseError) as error:
			print(error)


	def get_connection(self):
		if self.__connection is not None:
			print('Connection current open')
			return self.__connection
		else: return None


	def close_connection(self):
		if self.__connection is not None:
			self.__connection.close()
			print('Database connection closed.')
