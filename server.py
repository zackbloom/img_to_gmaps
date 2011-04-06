import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.web

application = tornado.web.Application([], 
    static_path=os.path.join(os.path.dirname(__file__), 'static'))

if __name__ == "__main__":
    serv = tornado.httpserver.HTTPServer(application)
    serv.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

