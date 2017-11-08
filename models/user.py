import sqlite3
from db import db
class UserModel(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self,name, password,):
         self.name = name
         self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(clc,name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(clc,_id):
        return cls.query.filter_by(name=_id).first()
