from src.model.user import User
import src.model.session
import json

def getUserList():
    return [{"id": 1, "name": "test"}]

def getUserById(id):
    print(id)
    return json.dumps(User.getUserById(id))
