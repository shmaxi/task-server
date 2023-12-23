import os
import logging
import tempfile


class BaseConfig(object):
    ENV = os.getenv('FLASK_ENV')
    CONFIG_ROOT = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False


class ProductionConfig(BaseConfig):
    DEBUG = False

    # DB
    DATABASE = 'users.db'
    USERNAME = 'admin'
    PASSWORD = 'Password13'

    # Redis
    REDIS_HOST = 'redis.production.shmax'
    REDIS_PORT = 6379


class LocalConfig(BaseConfig):
    DEBUG = True

    # DB
    DATABASE = 'users.db'
    USERNAME = 'admin'
    PASSWORD = 'Password12'

    # Redis
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

