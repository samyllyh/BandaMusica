import uuid
from flask import request
from models.endereco import Endereco


class New_Endereco:
    def new_endereco(cpf, transaction):
        try:
            request_from = request.json
            id = str(uuid.uuid4())
            novo_endereco = Endereco(
                id = id,
                rua = request_from["rua"],
                num_casa = request_from["num_casa"],
                bairro = request_from["bairro"],
                cpf = cpf
            )

            transaction.add(novo_endereco)
            return novo_endereco
        except Exception as e:
            raise e
        
    def list_all_endereco(cpf):
        try:
            endereco = Endereco.query.all()
            response = []

            for end in endereco:
                response.append(endereco.to_dict())
        except Exception as e:
            raise e
    
    def endereco_by_cpf(cpf):
        try:
            endereco = Endereco.query.get(cpf)
            if not endereco:
                   return f"CPF: {cpf} nao encontrado"
              
            return endereco
        except Exception as e:
            raise e
    
    def atualizar_endereco(endereco, transaction):
        try:
            request_form = request.json
            cpf = request_form["cpf"]
            enterprise = Endereco.query.get(cpf)

            enterprise.rua = request_form["rua"]
            enterprise.num_casa = request_form["num_casa"]
            enterprise.bairro = request_form["bairro"]

            transaction.add(enterprise)
            return enterprise

        except Exception as e:
            raise e
    
    def deletar_endereco(cpf, transaction):
        try:
            enredeco = Endereco.query.filter_by(cpf=cpf).delete()
            transaction.add(enredeco)
            print("Endereço deletado com sucesso")
        except Exception as e:
            raise e