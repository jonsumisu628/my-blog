import json

from src.model.session import session
from src.model.user import User


@session
def get_user_by_id(id, session=None):
    model = User.find_by_id(id, session)[0]
    result = json.dumps(model.to_dict())
    return result

@session
def get_user_list(session=None):
    model_list = User.find_all(session)
    result = json.dumps(list(map(lambda x: x.to_dict(), model_list)))
    return result

@session
def add_user(req_data, session=None):
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
    user = user.register(user, password, session)

    result = json.dumps(user.to_dict())
    return result

@session
def delete_user(id, session=None):
    pass
