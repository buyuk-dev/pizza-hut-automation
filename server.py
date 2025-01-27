from flask import Flask
from flask_restful import Resource, Api
import docker


app = Flask(__name__)
api = Api(app)


client = docker.from_env()


class PizzaOrder(Resource):
    def get(self):
        print("PizzaOrder - Start")
        try:
            client.containers.run("pizzahut:latest")
            print("PizzaOrder - Success")
            return {'status': 'order successful'}
        except Exception as e:
            print("PizzaOrder - Failure")
            return {'error': str(e)}


api.add_resource(PizzaOrder, '/pizza')


if __name__ == '__main__':
    app.run(debug=True, host="192.168.8.103", port=8000)

