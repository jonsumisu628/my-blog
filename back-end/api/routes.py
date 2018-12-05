from bottle import get

@get('/hello/<name>')
def index(name):
    print(name)
    return "Hello '%s'" % (name,)
