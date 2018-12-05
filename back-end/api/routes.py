from bottle import get

@get('/hello/<name>')
def index(name):
    return 'Hello {{name}}'
