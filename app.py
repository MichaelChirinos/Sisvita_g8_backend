from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from utils.db import db
from config import DATABASE_CONNECTION

from services.usuario import usuario_bp
from services.paciente import paciente
from services.especialista import especialista
from services.notificacion import notificacion
from services.persona import persona_bp
from services.historia_clinica import historia_clinica
from services.tipo_test import tipo_test
from services.pregunta import pregunta
from services.escala import escala
from services.evaluacion import evaluacion
from services.test import test
from services.alternativa import alternativa

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 20
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Cambia esta clave por una segura en producción

# Inicializa SQLAlchemy
db.init_app(app)

# Inicializa Flask-JWT-Extended
jwt = JWTManager(app)

# Registra los blueprints
app.register_blueprint(persona_bp)
app.register_blueprint(especialista)
app.register_blueprint(usuario_bp)
app.register_blueprint(paciente)
app.register_blueprint(notificacion)
app.register_blueprint(historia_clinica)
app.register_blueprint(tipo_test)
app.register_blueprint(pregunta)
app.register_blueprint(escala)
app.register_blueprint(test)
app.register_blueprint(evaluacion)
app.register_blueprint(alternativa)

# Crea las tablas si no existen
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
