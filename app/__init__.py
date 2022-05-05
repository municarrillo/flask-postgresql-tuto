from .global_routes import inicio as __inicio, dbstate as __dbstate
from .controllers import usuarios as __usuarios
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("config/flask_config.cfg")
app.register_blueprint(__dbstate)
app.register_blueprint(__inicio)
app.register_blueprint(__usuarios)
