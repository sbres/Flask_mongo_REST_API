from flask import Flask
from flask_restful import Api

from user.create import NewUser

app = Flask(__name__)
api = Api(app)

api.add_resource(NewUser, '/api/v1/user/new')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)