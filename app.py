from flask import Flask 
from utils.db import db
from flask_cors import CORS
from services.estudiante import estudiante
from services.respuestausuario import respuestausuario_bp
from services.respuestausuario2 import respuestausuario2_bp
from services.especialista import especialista
from services.usuario import usuario_bp
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 20
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800

#SQLAlchemy(app)
db.init_app(app)
app.register_blueprint(estudiante)
app.register_blueprint(respuestausuario_bp)
app.register_blueprint(respuestausuario2_bp)
app.register_blueprint(usuario_bp)


with app.app_context():
    db.create_all()


if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
