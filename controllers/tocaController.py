import uuid
from flask import request
from extensions import db
from models.eventos import Evento
from models.integrante import Integrante
from models.toca import Toca


class New_toca:
    def new_toca(transaction):
        try:
            request_form = request.json
            cpf = request_form["cpf"]
            envento_id = request_form["evento_id"]
            encontrarCPF = encontrar_cpf(cpf)
            encontrarEvento = encontrar_evento(envento_id)

            id = str(uuid.uuid4())
            novo_toca = Toca(
                id = id,
                cpf = encontrarCPF,
                evento_id = encontrarEvento
            )

            transaction.add(novo_toca)
            return novo_toca.to_dict()
        except Exception as e:
            raise e
    
    def list_toca_for_cpf_and_dia(cpf, evento_id):
        try:
            toca = Toca.query.filter_by(cpf=cpf, evento_id=evento_id).first()
            if not toca:
                return f"Quem toca no dia não foi encontrado para o CPF {cpf}"
            return toca.to_dict()
        except Exception as e:
            raise e
    
    """def atualizar_toca(id, transaction):
        try:
            request_form = request.json
            enterprise = Toca.query.get(id) 

            enterprise.cpf = request_form["cpf"]
            enterprise.evento_id = request_form["evento_id"]

            transaction.add(enterprise)
            return enterprise
        except Exception as e:
            raise e"""
    
    def deletar_toca(cpf, evento_id):
        try:
            toca = Toca.query.filter_by(cpf=cpf, evento_id=evento_id).first()
            if not toca:
                return f"Quem toca no dia não foi encontrado para o CPF {cpf}"
            db.session().delete(toca)

            db.session.commit()
            print("quem  deletado com sucesso")
        except Exception as e:
            raise e


def encontrar_cpf(cpf):
    try:
        encontrar = Integrante.query.filter_by(cpf=cpf).first()
        if not encontrar:
            return "Nao encontrado"
        return encontrar.cpf
    except Exception as e:
        raise e

def encontrar_evento(evento_id):
    try:
        encontrar = Evento.query.filter_by(id=evento_id).first()
        if not encontrar:
            return f"evento com o id: {evento_id} nao encontrado"
        return encontrar.id
    except Exception as e:
        raise e