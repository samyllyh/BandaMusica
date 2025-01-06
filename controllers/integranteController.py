from flask import request
from extensions import db

from mapper.integranteMapper import IntegranteMapper
from models.integrante import Integrante

class New_Integrante():
    def new_integrante(transaction):
        try:
            request_from = request.json
            cpf = request_from["cpf"]
            if verificar_cpf(cpf):
                raise ValueError("CPF já cadastrado!")
            novo_integrante = Integrante(
                    cpf = cpf,
                    nome = request_from['nome'],
                    funcao = request_from['funcao'],
                    situacao = request_from['situacao'],
                    responsavel = request_from['responsavel'],
                    maestro = request_from['maestro'],
                    regente = request_from['regente'],
                    cargo_banda = request_from['cargo_banda'],
                    iniciante_musicalidade = request_from['iniciante_musicalidade'],
                    intermediario_musicalidade = request_from['intermediario_musicalidade'],
                    avancado_musicalidade = request_from['avancado_musicalidade']
            )
            transaction.add(novo_integrante)
            return novo_integrante
        except Exception as e:
             raise e
             
    
    def list_all_integrante():
         try:
            integrantes = Integrante.query.all()
            response = []
            for integrante in integrantes:
                response.append(integrante.to_dict())

            return response
         except Exception as e:
              raise e
    
    def integrante_by_cpf(cpf):
         try:
              integrante = Integrante.query.get(cpf)
              if not integrante:
                   return f"CPF: {cpf} nao encontrado"
              
              return integrante.to_dict()
         except Exception as e:
              raise e
    
    def atualizar_integrante(cpf, transaction):
         try:
            request_form = request.json
            
            enterprise = Integrante.query.get(cpf)

            enterprise.nome = request_form["nome"]
            enterprise.funcao = request_form["funcao"]
            enterprise.situacao = request_form["situacao"]
            enterprise.responsavel = request_form["responsavel"]
            enterprise.maestro = request_form["maestro"]
            enterprise.cargo_banda = request_form["cargo_banda"]
            enterprise.iniciante_musicalidade = request_form["iniciante_musicalidade"]
            enterprise.intermediario_musicalidade = request_form["intermediario_musicalidade"]
            enterprise.avancado_musicalidade = request_form["avancado_musicalidade"]

            transaction.add(enterprise)
            return IntegranteMapper.integrante_mapper(enterprise)
         except Exception as e:
            raise e
    
    def deletar_integrante(cpf):
         try:
             integrante = Integrante.query.filter_by(cpf=cpf).first()
             print(integrante)

             if integrante.telefone:
                for telefone in integrante.telefone:
                    db.session.delete(telefone)

             if integrante.endereco:
                 db.session().delete(integrante.endereco)

             db.session().delete(integrante)

             db.session.commit()
             return "integrante deletado com sucesso"
         except Exception as e:
             raise e

         

def verificar_cpf(cpf):
        Integrante.query.filter_by(cpf=cpf).exists() is not None
