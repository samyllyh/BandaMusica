from flask import request
from extensions import db

from models.instrumento import Instrumento


class New_Instrumento:
    def new_instrumento(transaction):
        try:
            request_from = request.json
            novo_instrumento = Instrumento(
                nome_instrumento = request_from["nome_instrumento"],
                afinacao = request_from["afinacao"],
                marca = request_from["marca"],
                estado_fisico = request_from["estado_fisico"],
                natureza_instrumento = request_from["natureza_instrumento"]
            )
            transaction.add(novo_instrumento)
            return novo_instrumento
        except Exception as e:
            raise e
    
    def list_all_instrumentos():
        try:
            instrumentos = Instrumento.query.all()
            response = []
            for instrumento in instrumentos:
                response.append(instrumento.to_dict())
            
            return response
        except Exception as e:
            raise e
    
    def list_instrumento_by_id(id):
        try:
            instrumento = Instrumento.query.get(id)
            if not instrumento:
                    return f"Id: {id} nao encontrado"
              
            return instrumento.to_dict()
        except Exception as e:
            raise e
    
    def atualizar_instrumento(id, transaction):
        try:
            request_form = request.json
            
            enterprise = Instrumento.query.get(id)

            enterprise.nome_instrumento = request_form["nome_instrumento"]
            enterprise.afinacao = request_form["afinacao"]
            enterprise.marca = request_form["marca"]
            enterprise.estado_fisico = request_form["estado_fisico"]
            enterprise.natureza_instrumento = request_form["natureza_instrumento"]

            transaction.add(enterprise)
            return enterprise
        except Exception as e:
            raise e
    
    def deletar_instrumentos(id):
        try:
            instrumento = Instrumento.query.filter_by(id=id).first()
            db.session().delete(instrumento)

            db.session().commit()
            print("Instrumento deletado com sucesso")
        except Exception as e:
            raise e
