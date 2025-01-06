from flask import request
from extensions import db
from models.equipameto_suporte import EquipamentoSuporte
from models.integrante import Integrante
from models.utiliza import Utiliza


class New_Utiliza:
    def new_utuliza(transaction):
        try:
            request_form = request.json
            cpf = request_form["cpf"]
            equipamento_suporte_id = request_form["equipamento_suporte_id"]

            encontrarCPF = encontrar_cpf(cpf)
            encontrarSuporte = encontrar_equipamento(equipamento_suporte_id)

            novo_utiliza = Utiliza(
                cpf = encontrarCPF,
                equipamento_suporte_id = encontrarSuporte
            )
            transaction.add(novo_utiliza)
            return novo_utiliza.to_dict()
        except Exception as e:
            raise e
        
    def list_utiliza_by_cpf(cpf):
        try:
            utiliza = Utiliza.query.filter_by(cpf=cpf).first()
            if not utiliza:
                return f"Nao foi encontrado o cpf {cpf}"
            return utiliza.to_dict()
        except Exception as e:
            raise e
    
    """def atalizar_utiliza(id, transaction):
        try:
            request_form = request.json
            
            enterprise = Utiliza.query.get(id)

            enterprise.cpf = request_form["cpf"]
            enterprise.equipamento_suporte_id = request_form["equipamento_suporte_id"]

            transaction.add(enterprise)
            return enterprise
        except Exception as e:
            raise e"""
    
    def deletar_utiliza(cpf, equipamento_suporte_id):
        try:
            utiliza = Utiliza.query.filter_by(cpf=cpf, equipamento_suporte_id=equipamento_suporte_id).first()
            if not utiliza:
                return f"Quem utiliza o equipamento suporte: {equipamento_suporte_id}, nao foi encontrado para o CPF: {cpf}"

            db.session().delete(utiliza)

            db.session().commit()
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

def encontrar_equipamento(equipamento_id):
    try:
        encontrar = EquipamentoSuporte.query.filter_by(id=equipamento_id).first()
        if not encontrar:
            return "nao encontrado"
        return encontrar.id
    except Exception as e:
        raise e