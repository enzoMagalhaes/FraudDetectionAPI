from flask import Flask
from api.controller import prediction_app

def create_app():
	app = Flask("ml_api")

	app.register_blueprint(prediction_app)
	return app 