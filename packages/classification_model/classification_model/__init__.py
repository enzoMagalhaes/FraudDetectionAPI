from classification_model.config import config 

with open(config.VERSION_PATH,"r") as version:
	__version__ = version.read().strip()