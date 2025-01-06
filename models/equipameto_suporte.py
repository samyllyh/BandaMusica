from extensions import db

class EquipamentoSuporte(db.Model):
    __tablename__ = 'equipamento_suporte'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cera = db.Column(db.Boolean) # 1-sim / 0-nao
    cadeira = db.Column(db.Boolean)
    suporte = db.Column(db.Boolean)
    equipamento_extra = db.Column(db.Boolean)

    cpf = db.Column(db.String(11), db.ForeignKey("integrante.cpf"))

    def to_dict(self):
        return{
            'cera': bool(self.cera),
            'cadeira': bool(self.cadeira),
            'suporte': bool(self.suporte),
            'equipamento_extra': bool(self.equipamento_extra),
            'cpf': self.cpf
        }
    
    def __repr__(self):
        return f"<Equipamento_suporte cera={self.cera}, cadeira={self.cadeira}, suporte={self.suporte}, equipamento_extra={self.equipamento_extra}>"