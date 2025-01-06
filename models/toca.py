from extensions import db

class Toca(db.Model):
    __tablename__ = 'toca'
    id = db.Column(db.String(255), primary_key=True)
    cpf = db.Column(db.String(11), db.ForeignKey('integrante.cpf'))
    evento_id = db.Column(db.String(255), db.ForeignKey('eventos.id'))

    def to_dict(self):
        return {
            'cpf': self.cpf,
            'evento_id': self.evento_id
        }
    
    def __repr__(self):
        return f"<Toca cpf={self.cpf}, evento_id={self.evento_id}>"