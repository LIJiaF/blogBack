import tornado.web
import tornado.ioloop

from api import *
from config import tornadoConfig

url = [
    (r"/login", LoginHandle),
]


def make_app(url, config):
    app = tornado.web.Application(url, **config)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    make_app(url, tornadoConfig)
