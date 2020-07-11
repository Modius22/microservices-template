from flask_restplus import Resource

class application(Resource):
	def get(self):
		return "Hello World"

