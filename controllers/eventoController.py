from datetime import datetime
import uuid
from flask import request
from extensions import db

from models.eventos import Evento


class New_Evento:
    def new_evento(transaction):
        try:
            request_form = request.json
            id = str(uuid.uuid4())
            novo_evento = Evento(
                id = id,
                tipo_evento = request_form["tipo_evento"],
                dia = request_form["dia"],
                hora = request_form["hora"]
            )

            transaction.add(novo_evento)
            return novo_evento.to_dict()
        except Exception as e:
            raise e
    
    def list_all_eventos():
        try:
            eventos = Evento.query.all()
            response = []
            for evento in eventos:
                response.append(evento.to_dict())
            
            return response
        except Exception as e:
            raise e
    
    def list_evento_by_day(dia):
        try:
            eventos = Evento.query.filter(Evento.dia == dia).all()
            if not eventos:
                return f"Evento(s) do dia: {dia} nao encontrado"
            eventos_dict = [evento.to_dict() for evento in eventos]
            return eventos_dict
        except Exception as e:
            raise e
    
    def atualizar_evento(id, transaction):
        try:
            request_form = request.json

            tipo_evento = request_form["tipo_evento"]
            dia = request_form["dia"]
            hora = request_form["hora"]

            dia_obj = datetime.strptime(dia, "%Y-%m-%d").date()
            hora_obj = datetime.strptime(hora, "%H:%M:%S").time()

            enterprise = Evento.query.get(id)

            enterprise.tipo_evento = tipo_evento
            enterprise.dia = dia_obj
            enterprise.hora = hora_obj


            transaction.add(enterprise)
            return enterprise.to_dict()
        except Exception as e:
            raise e
    
    def deletar_evento(id):
        try: 
            evento  = Evento.query.filter_by(id=id).first()
            db.session().delete(evento)

            db.session.commit()
            print("Evento deletado com sucesso")
        except Exception as e:
            raise e