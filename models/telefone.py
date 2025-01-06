from extensions import db

class Telefone(db.Model):
    __tablename__ = 'telefone'
    num_telefone1 = db.Column(db.String(20), nullable=False)
    num_telefone2 = db.Column(db.String(20))

    cpf = db.Column(db.String(11), db.ForeignKey('integrante.cpf'), primary_key=True)

    def to_dict(self):
        return{
            'cpf': self.cpf,
            'num_telefone1': self.num_telefone1,
            'num_telefone2': self.num_telefone2
        }
    
    def __repr__(self):
        return f"<Telefone cpf={self.cpf}, num_telefone1={self.num_telefone1}, num_telefone2={self.num_telefone2}>"