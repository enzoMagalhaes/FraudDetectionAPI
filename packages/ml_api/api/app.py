from flask import Flask
from api.controller import prediction_app
from api.config import Config

import logging
_logger = logging.getLogger(__name__)


def create_app(*,config_object=Config):
	
	app = Flask("ml_api")

	app.config.from_object(config_object)
	app.register_blueprint(prediction_app)

	_logger.info("Application instance created")
	return app 