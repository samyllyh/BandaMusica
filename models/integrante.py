from extensions import db

class Integrante(db.Model):
    __tablename__ = 'integrante'
    cpf = db.Column(db.String(11), primary_key=True)
    nome = db.Column(db.String(40), nullable=False)
    funcao = db.Column(db.String(20), nullable=False)
    situacao = db.Column(db.Boolean) # 1-ativo / 0-inativo
    responsavel = db.Column(db.String(40))
    maestro = db.Column(db.Boolean) # 1-sim/0-nao
    regente = db.Column(db.Boolean) # 1-sim/0-nao
    cargo_banda = db.Column(db.String(50))
    iniciante_musicalidade = db.Column(db.Boolean) # 1-sim/0-nao
    intermediario_musicalidade = db.Column(db.Boolean) # 1-sim/0-nao
    avancado_musicalidade = db.Column(db.Boolean) # 1-sim/0-nao

    #RELACIONAMENTOS 
    endereco = db.relationship("Endereco", backref="integrante", uselist=False, cascade="all, delete")
    telefone = db.relationship("Telefone", backref="integrante", cascade="all, delete")
    eventos = db.relationship("Toca", backref="integrante", cascade="all, delete")
    equipamento = db.relationship("EquipamentoSuporte", backref="integrante", cascade="all, delete")

    def to_dict(self):
        return {
            'cpf': self.cpf,
            'nome': self.nome,
            'funcao': self.funcao,
            'situacao': self.situacao,
            'responsavel': self.responsavel,
            'maestro': self.maestro,
            'regente': self.regente,
            'cargo_banda': self.cargo_banda,
            'iniciante_musicalidade': self.iniciante_musicalidade,
            'intermediario_musicalidade': self.intermediario_musicalidade,
            'avancado_musicalidade': self.avancado_musicalidade,
        }
    def __repr__(self):
        return f"<Integrante cpf={self.cpf}, nome={self.nome}, funcao={self.funcao}>"