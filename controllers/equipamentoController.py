from flask import request
from extensions import db
from models.equipameto_suporte import EquipamentoSuporte


class New_Equipamentos:
    def new_equipamento(cpf, transaction):
        try:
            request_form = request.json
            equipamento = EquipamentoSuporte(
                cera = request_form["cera"],
                cadeira = request_form["cadeira"],
                suporte = request_form["suporte"],
                equipamento_extra = request_form["equipamento_extra"],
                cpf = cpf
            )
            transaction.add(equipamento)
            return equipamento.to_dict()
        except Exception as e:
            raise e
        
    def list_all_equipamentos():
        try:
            equipamentos = EquipamentoSuporte.query.all()
            response = []
            for equipamento in equipamentos:
                response.append(equipamento.to_dict())
            
            return response
        except Exception as e:
            raise e
    
    def equipamentos_by_cpf(cpf):
        try:
            equipamentos = EquipamentoSuporte.query.filter(cpf== cpf).first()
            if not equipamentos:
                return f"CPF: {cpf} nao encontrado"
            
            return equipamentos.to_dict()
        except Exception as e:
            raise e
    
    def atualizar_equipamentos(cpf, transaction):
        try:
            request_form = request.json
            
            enterprise = EquipamentoSuporte.query.filter(cpf== cpf).first()

            enterprise.cera = request_form["cera"]
            enterprise.cadeira = request_form["cadeira"]
            enterprise.suporte = request_form["suporte"]
            enterprise.equipamento_extra = request_form["equipamento_extra"]

            transaction.add(enterprise)
            return enterprise.to_dict()
        except Exception as e:
            raise e
    
    def deletar_equipamento(cpf):
        try:
            equipamento = EquipamentoSuporte.query.filter_by(cpf=cpf).first()
            db.session().delete(equipamento)

            db.session().commit()
            print("Equiepamento suporte deletado com sucesso")
        except Exception as e:
            raise e