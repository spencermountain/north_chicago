from flask import Flask

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from views import app

if __name__ == "__main__":
    server = HTTPServer(WSGIContainer(app))
    server.listen(5000)
    IOLoop.instance().start()

# app.run('0.0.0.0', debug=True)
