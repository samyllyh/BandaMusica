from extensions import db

class Endereco(db.Model):
    __tablename__ = 'endereco'
    id = db.Column(db.String(255), primary_key=True)
    rua = db.Column(db.String(30), nullable=False)
    num_casa = db.Column(db.Integer, nullable=False)
    bairro = db.Column(db.String(30), nullable=False)

    cpf = db.Column(db.String(11), db.ForeignKey("integrante.cpf"))

    def to_dict(self):
        return{
            'cpf': self.cpf,
            'rua': self.rua,
            'num_casa': self.num_casa,
            'bairro': self.bairro
        }
    
    def  __repr__(self):
        return f"<Endereco cpf={self.cpf}, rua={self.rua}, num_casa={self.num_casa}, bairro={self.bairro}>"