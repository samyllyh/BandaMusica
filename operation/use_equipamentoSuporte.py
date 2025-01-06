from controllers.equipamentoController import New_Equipamentos
from extensions import db
from flask import jsonify

class CreateEquipamentoSuporte:
    def create_equipamentoSuporte(cpf):
        transaction = db.session

        try:
            transaction.begin()

            equipamento = New_Equipamentos.new_equipamento(cpf, transaction)

            transaction.commit()

            return(
                jsonify(
                    {"message": "Equipamentos suporte criado com sucesso", "Equipamento Suporte": equipamento}
                )
            )
        
        except TypeError as e:
            transaction.rollback()
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            transaction.rollback()
            return jsonify({"error": f"Erro ao cadastrar novo equipamento suporte: {str(e)}"})
        
    def update_equipamentoSuporte(cpf):
        transaction = db.session

        try:
            transaction.begin()

            equipamento = New_Equipamentos.atualizar_equipamentos(cpf, transaction)

            transaction.commit()

            return(
                jsonify(
                    {"message": "Equipamento suporte atualizado com sucesso", "Equipamento Suporte": equipamento}
                )
            )
        
        except TypeError as e:
            transaction.rollback()
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            transaction.rollback()
            return jsonify({"error": f"Erro ao atualizar equipamento suporte: {str(e)}"})
        
    def delete_equipamentoSuporte(cpf):
        try:
            transaction = db.session()

            New_Equipamentos.deletar_equipamento(cpf)

            return(
                jsonify(
                    {"message": "Equipamento suporte excluido com sucesso" }
                )
            )
        
        except TypeError as e:
            transaction.rollback()
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            transaction.rollback()
            return jsonify({"error": f"Erro ao deletar equipamento suporte: {str(e)}"})
        
    def get_all_equipamentoSuporte():
        try:
            equipamento = New_Equipamentos.list_all_equipamentos()

            if not equipamento:
                return ( 
                        jsonify(
                            {"message": "Evento pesquisado não encontrada"}
                        ),
                        404,
                    )

            return(
                jsonify(
                    {"message": "Todos os equipamentos suporte", "Equipamentos suporte": equipamento}
                )
            )
        
        except TypeError as e:
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            return jsonify({"error": f"Erro ao buscar equipamento suporte: {str(e)}"})
    
    def get_equipamentoSuporte_by_cpf(cpf):
        try:
            equipamento = New_Equipamentos.equipamentos_by_cpf(cpf)

            if not equipamento:
                return ( 
                        jsonify(
                            {"message": "Evento pesquisado não encontrada"}
                        ),
                        404,
                    )
            
            return(
                jsonify(
                    {"message": "Equipamento suporte encontrado com sucesso", "Equipamento suporte": equipamento}
                )
            )
        
        except TypeError as e:
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            return jsonify({"error": f"Erro ao buscar equipamento suporte: {str(e)}"})
