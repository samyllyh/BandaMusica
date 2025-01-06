from flask import jsonify
from extensions import db
from controllers.enderecoController import New_Endereco
from controllers.integranteController import New_Integrante
from controllers.telefoneContoller import New_Telefone

class CreateIntegrate:
    def create_integrante():
        transaction = db.session

        try:
            transaction.begin()

            new_int = New_Integrante.new_integrante(transaction)
            _= New_Endereco.new_endereco(new_int.cpf, transaction)
            _= New_Telefone.new_telefone(new_int.cpf, transaction)

            transaction.commit()

            return (
                jsonify(
                    {"message": "Inegrante criado com sucesso", "cpf": new_int.cpf}
                ),
                200,
            ) 

        except TypeError as e:
            transaction.rollback()
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            transaction.rollback()
            return jsonify({"error": f"Erro ao cadastrar novo integrante: {str(e)}"})
        
    def update_integrante(cpf):
        transaction = db.session

        try:
            transaction.begin()
            
            integrante = New_Integrante.atualizar_integrante(cpf, transaction)
            endereco = integrante.get('endereco')
            telefones = integrante.get('telefones')
            _= New_Endereco.atualizar_endereco(endereco, transaction)
            _= New_Telefone.atualizar_telefone(telefones, transaction)

            transaction.commit()

            return (
                jsonify(
                    {"message": "Inegrante atualizado com sucesso", "Integrante":integrante}
                ),
                200
            )
        except TypeError as e:
            transaction.rollback()
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            transaction.rollback()
            return jsonify({"error": f"Erro ao atualizar dados do integrante: {str(e)}"})
    
    def deletar_integrante(cpf):
        transaction = db.session

        try:
            transaction.begin()

            integrante = New_Integrante.deletar_integrante(cpf)

            return(
                jsonify(
                    {"message": "Itegrante deletado com sucesso"}
                )
            )
        except TypeError as e:
            transaction.rollback()
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            transaction.rollback()
            return jsonify({"error": f"Erro ao atualizar dados do integrante: {str(e)}"})
    
    def buscar_integrante(cpf):
        try:
            integrante = New_Integrante.integrante_by_cpf(cpf)
            if not integrante:
                return ( 
                        jsonify(
                            {"message": "Integrante pesquisado não encontrada", "CPF": cpf}
                        ),
                        404,
                    )
            
            return(
                jsonify(
                    {"message": "Integrante encontrado com secesso", "Integrante": integrante }
                )
            )
        except TypeError as e:
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            return jsonify({"error": f"Erro ao atualizar dados do integrante: {str(e)}"})
    
    def buscar_all_integrante():
        try:
            integrante = New_Integrante.list_all_integrante()
            if not integrante:
                return ( 
                        jsonify(
                            {"message": "Integrante pesquisado não encontrada"}
                        ),
                        404,
                    )
            
            return(
                jsonify(
                    {"message": "Integrante encontrado com secesso", "Integrante": integrante }
                )
            )
        except TypeError as e:
            return jsonify({"error": f"Erro no tipo da variavel: {str(e)}"})
        except Exception as e:
            return jsonify({"error": f"Erro ao atualizar dados do integrante: {str(e)}"})