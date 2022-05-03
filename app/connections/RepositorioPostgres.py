import psycopg
from configparser import ConfigParser
from pathlib import Path


class Postgres():
	""" Connect to the PostgreSQL database server """
	connection = None

	def __init__(self):
		try:
			params = self.config()

			if self.connection is None:
				print('Connecting to the PostgreSQL database...')
				self.connection = psycopg.connect(**params)
			
		except (Exception, psycopg.DatabaseError) as error:
			print(error)


	def config(self, filename=Path(__file__).parents[1].name + '/config/config.ini', section='postgresql'):
		parser = ConfigParser()
		parser.read(filename)
	
		# get section, default to postgresql
		db = {}
		if parser.has_section(section):
			params = parser.items(section)
			for param in params:
				db[param[0]] = param[1]
		else:
			raise Exception('Section {0} not found in the {1} file'.format(section, filename))
	
		return db


	def get_connection(self):
		if self.connection is not None:
			print('Connection current open')
			return self.connection
		else: return None


	def close_conexion(self):
		if self.connection is not None:
			self.connection.close()
			print('Database connection closed.')
