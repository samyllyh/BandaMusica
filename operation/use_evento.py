from controllers.eventoController import New_Evento
from extensions import db
from flask import jsonify

class CreateEvento:
    def create_evento():
        transaction = db.session

        try:
            transaction.begin()

            evento = New_Evento.new_evento(transaction)

            transaction.commit()

            return (
                jsonify(
                    {"message": "evento criado com sucesso", "evento": evento}
                ), 200
            )
        except TypeError as e:
            transaction.rollback()
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            transaction.rollback()
            return jsonify({"error": f"Erro ao cadastrar novo evento: {str(e)}"})
    
    def update_evento(id):
        transaction = db.session

        try:
            transaction.begin()

            evento = New_Evento.atualizar_evento(id, transaction)

            transaction.commit()

            return(
                jsonify(
                    {"message": "Dados de evento atualizado com sucesso", "evento": evento}
                )
            )
        except TypeError as e:
            transaction.rollback()
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            transaction.rollback()
            return jsonify({"error": f"Erro ao atualizar dados de evento: {str(e)}"})
    
    def delete_evento(id):
        try:
            transaction = db.session()

            New_Evento.deletar_evento(id)

            return (
                jsonify(
                    {"message": "evento deletado com sucesso"}
                )
            )
        except TypeError as e:
            transaction.rollback()
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            transaction.rollback()
            return jsonify({"error": f"Erro ao deletar evento: {str(e)}"})
    
    def get_all_eventos():
        try:
            evento = New_Evento.list_all_eventos()

            if not evento:
                return ( 
                        jsonify(
                            {"message": "Evento pesquisado não encontrada"}
                        ),
                        404,
                    )
            
            return(
                jsonify(
                    {"message": "Evento encontrado com secesso", "Evento": evento }
                )
            )
        except TypeError as e:
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            return jsonify({"error": f"Erro ao buscar Evento: {str(e)}"})
    
    def get_evento_by_day(dia):
        try:
            evento = New_Evento.list_evento_by_day(dia)

            return (
                jsonify(
                    {"message": f"Eventos para o dia {dia} encontrado", "Evento": evento}
                )
            )
        except TypeError as e:
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            return jsonify({"error": f"Erro ao buscar Evento: {str(e)}"})