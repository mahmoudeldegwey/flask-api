import sqlite3
from flask import Flask,request
from flask_restful import Resource
from models.user import UserModel
class userRegister(Resource):

    def post(self):
        data = request.get_json()
        if UserModel.find_by_name(data['name']):
            return {'message':'user already exist'} , 400

        user = UserModel(**data)
        user.save_to_db()
        return {'message':'created successfully'},201
