from ma import ma
from models.hero import HeroModel

class HeroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = HeroModel
        load_instance = True