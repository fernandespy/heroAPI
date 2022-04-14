from flask import request
from flask_restx import Resource, fields
from models.hero import HeroModel
from schemas.hero import HeroSchema
from server.instance import server

hero_ns = server.hero_ns

hero_schema = HeroSchema()
hero_list_schema = HeroSchema(many = True)

HERO_NOT_FOUND = 'Hero not found!'

item = hero_ns.model('Hero', {
    'name': fields.String('Hero name'),
    'universe': fields.String('Hero universe'),
    'group': fields.String('Hero group')
})


class Hero(Resource):
    
    def get(self, id):
        hero_data = HeroModel.find_by_id(id)
        if hero_data:
            return hero_schema.dump(hero_data)
        return {'message': HERO_NOT_FOUND}, 404
    
    def delete(self, id):
        hero_data = HeroModel.find_by_id(id)
        if hero_data:
            hero_data.delete_from_db()
            return '', 204
        return {'message': HERO_NOT_FOUND}, 404
    
    @hero_ns.expect(item)
    def put(self, id):
        hero_data = HeroModel.find_by_id(id)
        hero_json = request.get_json()

        if hero_data:
            hero_data.name = hero_json['name']
            hero_data.universe = hero_json['universe']
            hero_data.group = hero_json['group']
        else:
            hero_data = hero_schema.load(hero_json)

        hero_data.save_to_db()
        return hero_schema.dump(hero_data), 200
    
class HeroList(Resource):
    @hero_ns.doc('Get all the Items')
    def get(self):
        return hero_list_schema.dump(HeroModel.find_all()), 200

    @hero_ns.expect(item)
    @hero_ns.doc('Create an Item')
    def post(self):
        hero_json = request.get_json()
        hero_data = hero_schema.load(hero_json)

        hero_data.save_to_db()

        return hero_schema.dump(hero_data), 201