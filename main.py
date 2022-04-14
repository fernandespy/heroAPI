from flask import Flask, Blueprint, jsonify
from marshmallow import ValidationError

from ma import ma
from db import db

from resources.hero import Hero, HeroList, hero_ns

from server.instance import server

app = server.app
api = server.api

@app.before_first_request
def create_tables():
    db.create_all()

@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400

api.add_resource(Hero, '/heros/<int:id>')
api.add_resource(HeroList, '/heros')


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()    
    
