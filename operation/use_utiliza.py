from flask import jsonify
from controllers.utilizaController import New_Utiliza
from extensions import db

class CreateUtiliza:
    def create_utiliza():
        transaction = db.session
        try:
            transaction.begin()

            utiliza = New_Utiliza.new_utuliza(transaction)

            transaction.commit()

            return (
                jsonify(
                    {"message": "quem utiliza os equipamentos extras criado com sucesso", "Utiliza": utiliza}
                )
            )
        
        except TypeError as e:
            transaction.rollback()
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            transaction.rollback()
            return jsonify({"error": f"Erro ao cadastrar quem utiliza: {str(e)}"})
    
    def delete_utiliza(cpf, equipamento_id):
        transaction = db.session
        try:
            New_Utiliza.deletar_utiliza(cpf, equipamento_id)

            return(
                jsonify(
                    {"message": "Quem utiliza o equipamento deletado com sucesso"}
                )
            )
        
        except TypeError as e:
            transaction.rollback()
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            transaction.rollback()
            return jsonify({"error": f"Erro ao cadastrar quem utiliza: {str(e)}"})
    
    def get_utiliza_by_cpf(cpf):
        try:
            utiliza = New_Utiliza.list_utiliza_by_cpf(cpf)

            if not utiliza:
                return(
                    jsonify(
                        {"message": "Quem precisa de equipamento suporte nao encontrado encontrado"}
                    )
                )
            
            return(
                jsonify(
                    {"message": "Quem precisa de equipamento suporte encontrado com sucesso", "Utiliza": utiliza}
                )
            )
        
        except TypeError as e:
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            return jsonify({"error": f"Erro ao cadastrar quem utiliza: {str(e)}"})
