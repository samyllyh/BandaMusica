from datetime import date
from extensions import db

class Evento(db.Model):
    __tablename__ = 'eventos'
    id = db.Column(db.String(255), primary_key=True)
    tipo_evento = db.Column(db.String(20), nullable=False)
    dia = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)

    def to_dict(self):
        return{
            'id': self.id,
            'tipo_evento': self.tipo_evento,
            "dia": self.dia.isoformat() if isinstance(self.dia, date) else self.dia,
            'hora': self.hora.isoformat() if self.hora else None
        }
    
    def __repr__(self):
        return f"<Evento tipo_evento={self.tipo_evento}, dia={self.dia}, hora={self.hora}>"