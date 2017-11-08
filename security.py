from resources.user import User
from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(name, password):
    user = UserModel.find_by_name(name)

    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
