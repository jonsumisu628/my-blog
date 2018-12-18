import json

from src.model.session import Session
from src.model.user import User


def get_user_by_id(id):
    session = Session()
    model = User.find_by_id(id, session)[0]
    session.close()
    result = json.dumps(model.to_dict())
    return result

def get_user_list():
    session = Session()
    model_list = User.find_all(session)
    session.close()
    result = json.dumps(list(map(lambda x: x.to_dict(), model_list)))
    return result

def add_user(req_data):
    email        = req_data['email']
    name         = req_data['name']
    display_name = req_data['display_name']
    avatar_url   = req_data['avatar_url']
    password     = req_data['password']

    user = User(
        email=email,
        name=name,
        display_name=display_name,
        avatar_url=avatar_url
    )
    session = Session()
    user = user.register(user, password, session)
    session.close()

    result = json.dumps(user.to_dict())
    return result

def delete_user(id):
    pass
