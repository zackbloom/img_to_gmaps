import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.web

class ImgHandler(tornado.web.RequestHandler):
    def get(self, zoom, x, y):
        print zoom, x, y

application = tornado.web.Application([
    (r"/cart_imgs/(%d)/(%d)/(%d)\.png", ImgHandler),
], static_path=os.path.join(os.path.dirname(__file__), 'static'))

if __name__ == "__main__":
    serv = tornado.httpserver.HTTPServer(application)
    serv.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

