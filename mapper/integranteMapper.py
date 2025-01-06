class IntegranteMapper:
    def integrante_mapper(integrante):
        try:
            integrante_dict = {
                "nome": integrante.nome,
                "cpf": integrante.cpf,
                "funcao": integrante.funcao,
                "situacao": integrante.situacao,
                "responsavel": integrante.responsavel,
                "maestro": integrante.maestro,
                "regente": integrante.regente,
                "cargo_banda": integrante.cargo_banda,
                "iniciante_musicalidade": integrante.iniciante_musicalidade,
                "intermediario_musicalidade": integrante.intermediario_musicalidade,
                "endereco": integrante.endereco.to_dict() if integrante.endereco else None,
                "telefones": [telefone.to_dict() for telefone in integrante.telefone],
            }
            return integrante_dict
        except Exception as e:
            raise e