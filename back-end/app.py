import bottle
import src.setting
import src.routes

if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port=80, reloader=True, debug=True)
