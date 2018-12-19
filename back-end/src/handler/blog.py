import logging
from logging import getLogger

from src.model.blog import Blog
from src.model.session import session

logger = getLogger("my-blog").getChild(__name__)

@session
def get_blog_by_id(id, session=None):
    model = Blog.find_by_id(id, session)
    result = model.to_dict()
    return result

@session
def get_blog_list(session=None):
    model_list = Blog.find_all(session)
    result = list(map(lambda x: x.to_dict(), model_list))
    return result

@session
def add_blog(blog, session=None):
    pass

@session
def delete_blog(id, session=None):
    pass
