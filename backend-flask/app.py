from flask import Flask
from flask_cors import CORS

from flask_restplus import reqparse, Api
from src import routes

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)
parser = reqparse.RequestParser()

api.add_resource(routes.application, '/test')

if __name__ == '__main__':
    app.run()