import logging
import os

from flask import Flask, Blueprint
from flask_cors import CORS
from flask_restx import Api

from api.v1.config import CONFIG_NAME_MAPPER, CURRENT_CONFIG
from api.v1.resources.tasks import ns as task_ns
from utils.logger import setup_logging


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    set_app_config(app)
    
    if test_config is None:
        app.config['CORS_HEADERS'] = 'Content-Type'
    else:
        # load the test config if passed in
        app.config.from_object(test_config)

    CORS(app, resources={r'/*': {'origins': '*'}})

    # attach headers
    @app.after_request
    def headers(resp):
      resp.headers['Content-Security-Policy']='default-src \'self\''
      resp.headers['X-XSS-Protection'] = '1; mode=block'
      resp.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains; preload'
      resp.headers['X-Frame-Options'] = 'SAMEORIGIN'
      resp.headers['X-Content-Type-Options'] = 'nosniff'
      resp.headers['Server'] = 'LNC'
      resp.headers['is-unicorn'] = 'true'
      return resp

    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

    authorizations = {
        'apikey': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    }

    api = Api(
        blueprint,
        appversion='1.0',
        title='Task Server REST API',
        description='The best backend in the world',
        security='apikey', 
        authorizations=authorizations
    )

    api.add_namespace(task_ns)

    app.register_blueprint(blueprint)

    return app


def set_app_config(app):
    log_level = logging.INFO
    if CURRENT_CONFIG.DEBUG:
        log_level = logging.DEBUG

    setup_logging(default_level=log_level)

    flask_env_name = os.getenv('FLASK_ENV')
    if flask_env_name is None:
        flask_env_name = 'local'

    app.flask_config_name = flask_env_name
    # log.info("Running app on %s env" % CONFIG_NAME_MAPPER[flask_env_name])
    app.config.from_object(CONFIG_NAME_MAPPER[flask_env_name])
