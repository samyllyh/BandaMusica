from flask import request
from models.telefone import Telefone


class New_Telefone:
    def new_telefone(cpf, transaction):
        try:
            request_form = request.json
            novo_telefone = Telefone(
                num_telefone1 = request_form["num_telefone1"],
                num_telefone2 = request_form["num_telefone2"],
                cpf = cpf
            )
            transaction.add(novo_telefone)
            return novo_telefone
        except Exception as e:
            raise e
        
    def telefone_by_cpf(cpf):
        try:
            telefone = Telefone.query.get(cpf)
            if not telefone:
                return f"CPF: {cpf} nao encontrado"
            return telefone
        except Exception as e:
            raise e
    
    def  atualizar_telefone(telefone, transaction):
        try:
            request_form = request.json
            cpf = request_form["cpf"]
            enterprise = Telefone.query.get(cpf)

            enterprise.num_telefone1 = request_form["num_telefone1"]
            enterprise.num_telefone2 = request_form["num_telefone2"]

            transaction.add(enterprise)
            return enterprise 
        except Exception as e:
            raise e
    
    def deletar_telefone(cpf, transaction):
        try:
            telefone = Telefone.query.filter_by(cpf=cpf).delete()
            transaction.add(telefone)
            return "Telefone deletado com sucesso"
        except Exception as e:
            raise e
