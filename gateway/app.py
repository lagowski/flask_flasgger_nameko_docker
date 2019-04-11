from flask import Flask, Blueprint, jsonify
from flasgger import Swagger
from flask_restful import Api, Resource

from resources.resource1 import Say, Time


def routes(api):
  api.add_resource(Index, "/v1", endpoint="index")
  api.add_resource(Say, "/v1/say", "/v1/say/<string:text2say>",
                   endpoint="say")
  api.add_resource(Time, "/v1/time",
                   endpoint="time")



def main(host, port, debug):
  app.run(host, port, debug)


class Index(Resource):
  def get(self):
    return {"response": "API Working"}


# Init of Flask Application
app = Flask(__name__)
swagger = Swagger(app)
app.register_blueprint(Blueprint('api', __name__))
routes(Api(app))

if __name__ == "__main__":
  main(host='0.0.0.0', port=5000, debug=True)
