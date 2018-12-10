from setting import session
from src.table import user

def getUserById(id):
    users = session.query(user.User)
    for user in users:
        print(user.name)
    return {"id": id, "name": "test"}

def addUser(user):
    user = user.User()
    user.name = 'とも太郎'
    session.add(user)
    session.commit()
