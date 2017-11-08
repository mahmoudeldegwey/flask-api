import sqlite3
from flask_restful import Resource
from flask_jwt import jwt_required
from models.item import ItemModel

class items(Resource):
    @jwt_required
    def get(self, name):

        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'item not found'}, 404

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message': ' the user is already exists'}

        data = request.get_json()
        item = ItemModel(name,data['price'] )

        try:
            item.save_to_db()
        except:
            return {'message':  'An error occured inserting the item'}, 200
        return item.json(),201

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item :
            item.delete_from_db()

        return {'message':'item deleted'}

    def put(self,name):
        data = request.get_json()
        item = self.find_by_name(name)

        if item is None:
            try:
                item = ItemModel(name, data['price'])
        else:
                item.price = data['price']
        item.save_to_db()
        return item.json()



class ItemList(Resource):
    def get(self):
    return {'item':[x.json() for item in ItemModel.query.all() ]}
