import json

from bottle import get

from src.handler import blog, user


@get('/users')
def listUser():
    return json.dumps(user.get_user_list())

@get('/users/<id>')
def showUser(id):
    return json.dumps(user.get_user_by_id(id))

@get('/blog')
def listBlog():
    return json.dumps(blog.get_blog_list())

@get('/blog/<id>')
def showBlog(id):
    return json.dumps(blog.get_blog_by_id(id))
