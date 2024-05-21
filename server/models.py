from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.Integer)
    price = db.Column(db.Integer)
    
    
    def __repr__(self):
        return f'<plant {self.name} , {self.image}, {self.price}. >'
    
