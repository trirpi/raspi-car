# -*- coding: utf-8 -*-
import settings


def run():
    from gevent import monkey
    monkey.patch_all()

    from gevent.pywsgi import WSGIServer
    from rcar import app

    http_server = WSGIServer((settings.bind_host, settings.bind_port), app)
    print ' * Running on http://%s:%s/ (Press CTRL+C to quit)' % (settings.bind_host, str(settings.bind_port))
    http_server.serve_forever()

if __name__ == '__main__':
    run()
