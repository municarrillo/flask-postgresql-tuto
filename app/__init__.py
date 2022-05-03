from .routes import tienda as __tienda, cliente as __cliente
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("config/flask_config.cfg")
app.register_blueprint(__tienda)
app.register_blueprint(__cliente)
