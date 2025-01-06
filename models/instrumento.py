from extensions import db

class Instrumento(db.Model):
    __tablename__ = 'instrumento'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_instrumento = db.Column(db.String(30), nullable=False)
    afinacao = db.Column(db.String(30), nullable=False)
    marca = db.Column(db.String(30), nullable=False)
    estado_fisico = db.Column(db.String(20), nullable=False)
    natureza_instrumento = db.Column(db.String(20), nullable=False)


    def to_dict(self):
        return{
            'nome_instrumento': self.nome_instrumento,
            'afinacao': self.afinacao,
            'marca': self.marca,
            'estado_fisico': self.estado_fisico,
            'natureza_instrumento': self.natureza_instrumento
        }
    
    def __repr__(self):
        return f"<Instrumento nome_instrumento={self.nome_instrumento}, marca={self.marca}, estado_fisico={self.estado_fisico}, natureza_instrumento={self.natureza_instrumento}>"