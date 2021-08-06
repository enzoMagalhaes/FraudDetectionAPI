from api.app import create_app
from api.config import Config,setup_app_logging

_config = Config()
setup_app_logging(config=_config)

application = create_app(config_object=_config)

if __name__ == "__main__":
	 application.run(port=_config.SERVER_PORT, host=_config.SERVER_HOST)