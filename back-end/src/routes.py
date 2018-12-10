import json

from bottle import get

from src.handler import blog, user


@get('/users')
def listUser():
    return json.dumps(user.getUserList())

@get('/users/<id>')
def showUser(id):
    return json.dumps(user.getUserById(id))

@get('/blog')
def listBlog():
    return json.dumps(blog.getBlogList())

@get('/blog/<id>')
def showBlog(id):
    return json.dumps(blog.getBlogById(id))
