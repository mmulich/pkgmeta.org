import os
from paste.deploy import loadapp
from wsgiref.simple_server import make_server

here = os.path.abspath(os.path.dirname(__file__))
wsgi_app = loadapp('config:%s' % os.path.join(here, 'development.ini'))
httpd = make_server('', 6543, wsgi_app)
httpd.serve_forever()
