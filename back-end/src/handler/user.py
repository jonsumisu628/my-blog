import json

from src.model.session import Session
from src.model.user import User


def get_user_by_id(id):
    session = Session()
    model = User.find_by_id(id, session)
    session.close()
    result = json.dumps(model.to_dict())
    return result

def get_user_list():
    session = Session()
    model_list = User.find_all(session)
    session.close()
    result = json.dumps(list(map(lambda x: x.to_dict(), model_list)))
    return result
