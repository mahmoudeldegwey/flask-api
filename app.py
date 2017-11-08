from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import userRegister
from resources.item import items,ItemList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_rquest
def create_tables():
    db.create_all()

app.secrect_key = "mahmoud"
jwt = JWT(app,authenticate,identity)

api.add_resource(items, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(userRegister,'/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
