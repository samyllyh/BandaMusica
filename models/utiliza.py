from extensions import db

class Utiliza(db.Model):
    __tablename__ = 'utiliza'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf = db.Column(db.String(11), db.ForeignKey('integrante.cpf'))
    equipamento_suporte_id = db.Column(db.Integer, db.ForeignKey('equipamento_suporte.id'))

    def to_dict(self):
        return {
            'cpf': self.cpf,
            'equipamento_suporte_id': self.equipamento_suporte_id
        }
    
    def __repr__(self):
        return f"<Utiliza cpf={self.cpf}, equipamento_suporte_id={self.equipamento_suporte_id}>"