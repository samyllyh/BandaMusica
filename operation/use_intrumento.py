from extensions import db
from flask import jsonify

from controllers.instrumentoController import New_Instrumento

class CreateInstrumento:
    def create_instrumento():
        try:
            transaction = db.session()

            instrumento = New_Instrumento.new_instrumento(transaction)

            transaction.commit()

            return (
                jsonify(
                    {"message": "Intrumento criado com sucesso", "id": instrumento.id}
                ), 200
            )
        except TypeError as e:
            transaction.rollback()
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            transaction.rollback()
            return jsonify({"error": f"Erro ao cadastrar novo instrumento  : {str(e)}"})
        
    def update_instrumento(id):
        try:
            transaction = db.session()

            instrumento = New_Instrumento.atualizar_instrumento(id, transaction)

            transaction.commit()
            return(
                jsonify(
                    {"message": "Dados atualizados com sucesso", "Id": instrumento.id}
                )
            )
        except TypeError as e:
            transaction.rollback()
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            transaction.rollback()
            return jsonify({"error": f"Erro ao atualizar instrumento: {str(e)}"})
    
    def delete_instrumento(id):
        try:
            transaction = db.session()

            New_Instrumento.deletar_instrumentos(id)

            return(
                jsonify(
                    {"messagem": "Instrumento deletado com sucesso"}
                )
            )
        except TypeError as e:
            transaction.rollback()
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            transaction.rollback()
            return jsonify({"error": f"Erro ao deletar instrumento: {str(e)}"})
    
    def buscar_instrumento(id):
        try:
            instrumento = New_Instrumento.list_instrumento_by_id(id)

            if not instrumento:
                return ( 
                        jsonify(
                            {"message": "Instrumento pesquisado não encontrada", "ID": id}
                        ),
                        404,
                    )
            
            return(
                jsonify(
                    {"message": "Instrumento encontrado com secesso", "Instrumento": instrumento }
                )
            )
        
        except TypeError as e:
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            return jsonify({"error": f"Erro ao buscar instrumento: {str(e)}"})
    
    def buscar_all_instrumento():
        try:
            instrumento = New_Instrumento.list_all_instrumentos()

            if not instrumento:
                return ( 
                        jsonify(
                            {"message": "Instrumentos pesquisado não encontrada"}
                        ),
                        404,
                    )
            
            return(
                jsonify(
                    {"message": "instrumentos encontrado com secesso", "instrumento": instrumento }
                )
            )
        except TypeError as e:
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            return jsonify({"error": f"Erro ao buscar instrumentos: {str(e)}"})


