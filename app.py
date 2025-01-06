from flask import Flask, request, jsonify
from flask_cors import CORS
from routes import api_bp
from extensions import db, migrate

def create_app():
    app = Flask(__name__)
    
    # Configuração do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1903@localhost:5432/banda-musica'
    
    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(api_bp)

    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    return app

app = create_app()
from models import (Integrante, Telefone, Endereco, EquipamentoSuporte, Evento, Instrumento, Responsavel, Toca, Utiliza)
if __name__ == "__main__":
    app.run(debug=True)

