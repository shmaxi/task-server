import api.v1.config.config
import os

CONFIG_NAME_MAPPER = {
    'prod': config.ProductionConfig,
    'local': config.LocalConfig,
}


def get_current_config():
    flask_env_name = os.getenv('FLASK_ENV')
    if flask_env_name is None:
        flask_env_name = 'local'

    # log.info("Running app on %s env" % CONFIG_NAME_MAPPER[flask_env_name])
    return CONFIG_NAME_MAPPER[flask_env_name]()


CURRENT_CONFIG = get_current_config()
