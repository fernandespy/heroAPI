from db import db
from typing import List

class HeroModel(db.Model):
    __tablename__ = 'heros'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32), nullable = False, unique = True)
    universe = db.Column(db.String(50), nullable = False)
    group = db.Column(db.String(50), nullable = True)

    def __init__(self, name, universe, group):
        self.name = name
        self.universe = universe
        self.group = group

    def __repr__(self, ):
        return f'HeroModel(name={self.name}, universe={self.universe}, group={self.group}'

    def json(self, ):
        return {
            'name': self.name,
            'universe': self.universe,
            'group': self.universe
        }
        
    @classmethod
    def find_by_name(cls, name) -> "HeroModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id) -> "HeroModel":
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_all(cls) -> List["HeroModel"]:
        return cls.query.all()
    
    def save_to_db(self, ) -> None:
        db.session.add(self)
        db.session.commit()
            
    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()