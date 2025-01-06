from extensions import db

class Responsavel(db.Model):
    __tablename__ = 'responsavel'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    cpf = db.Column(db.String(11), db.ForeignKey('integrante.cpf'), primary_key=True)
    instrumento_id = db.Column(db.Integer, db.ForeignKey('instrumento.id'), primary_key=True)


    def to_dict(self):
        return{
            'cpf': self.cpf,
            'instrumento_id': self.instrumento_id
        }
    
    def __repr__(self):
        return f"<Responsvel cpf={self.cpf}, instrumento_id={self.instrumento_id}>"