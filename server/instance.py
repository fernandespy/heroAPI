from flask import Flask, Blueprint
from flask_restx import Api

class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc = '/doc', title = 'Sample Hero API')
        self.app.register_blueprint(self.blueprint)
        
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['PROPAGATE_EXECEPTIONS'] = True

        self.hero_ns = self.hero_ns()
        
        super().__init__()

    def hero_ns(self):
        return self.api.namespace(name = 'heros', description = 'Heros related operations', path = '/')

    def run(self, ):
        self.app.run(
            port = 5000,
            debug = True,
            host = '0.0.0.0'
        )

server = Server()

