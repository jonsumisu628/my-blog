import json

from src.model.blog import Blog
from src.model.session import Session


def get_blog_by_id(id):
    session = Session()
    model = Blog.find_by_id(id, session)
    session.close()
    result = json.dumps(model.to_dict())
    return result

def get_blog_list():
    session = Session()
    model_list = Blog.find_all(session)
    session.close()
    result = json.dumps(list(map(lambda x: x.to_dict(), model_list)))
    return result

def add_blog(blog):
    pass

def delete_blog(id):
    pass
