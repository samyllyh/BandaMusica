from flask import jsonify
from controllers.tocaController import New_toca
from extensions import db

class CreateToca:
    def create_toca():
        transaction = db.session
        try:
            transaction.begin()

            toca = New_toca.new_toca(transaction)

            transaction.commit()

            return(
                jsonify(
                    {"message": "quem toca criado com sucesso", "toca": toca}
                )
            )
        
        except TypeError as e:
            transaction.rollback()
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            transaction.rollback()
            return jsonify({"error": f"Erro ao cadastrar quem toca: {str(e)}"})
    
    def delete_toca(cpf, dia):
        try:
            transaction = db.session()

            New_toca.deletar_toca(cpf, dia)

            return(
                jsonify(
                    {"message": f"Quem toca no dia {dia} com o cpf {cpf} foi deletado com sucesso" }
                )
            )
        except TypeError as e:
            transaction.rollback()
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            transaction.rollback()
            return jsonify({"error": f"Erro ao deletar quem toca: {str(e)}"})
    
    def get_toca_by_day_and_cpf(cpf, dia):
        try:
            toca = New_toca.list_toca_for_cpf_and_dia(cpf, dia)

            if not toca:
                return(
                    jsonify(
                        {"message": f"Nao foi encontrado a pessoa com o cpf {cpf} que toca no dia {dia}"}
                    )
                )
            
            return(
                jsonify(
                    {"message": f"Quem toca toca no dia encontrado com sucesso", "Toca": toca}
                )
            )
        except TypeError as e:
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            return jsonify({"error": f"Erro ao buscar quem toca: {str(e)}"})