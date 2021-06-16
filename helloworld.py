from flask import Flask, request
from flask_restful import Resource, Api
from ddtrace import tracer

import logging
FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
          '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
          '- %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger(__name__)

app = Flask(__name__)
api = Api(app)

tracer.configure(
    hostname='host.docker.internal',
    port=8126,
)

class Greeting (Resource):
    @tracer.wrap()
    def get(self):
        log.info('Rota Greeting acessada')
        return 'Hello World!'

class Ping (Resource):
    @tracer.wrap()
    def get(self):
        log.info('Rota ping acessada')
        return 'Pong!'

api.add_resource(Greeting, '/home') # Route_1
api.add_resource(Ping, '/ping') # Route_2

if __name__ == '__main__':
    app.run('0.0.0.0','80')



