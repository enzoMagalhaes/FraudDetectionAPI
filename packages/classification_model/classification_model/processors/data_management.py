from classification_model.config import config

import logging
_logger = logging.getLogger(__name__)

def load_dataset(filename="audit_data.csv"):
	import pandas as pd
	df = pd.read_csv(config.DATASETS_DIR/filename)
	df = df.drop(["Score_B.1"],axis=1)

	return df 

def save_model(model,model_name=config.MODEL_NAME):
	import joblib

	joblib.dump(model,config.MODELS_DIR/model_name)
	_logger.info(f"saved model: {model_name}")

def load_model(model_name=config.MODEL_NAME):
	import joblib 
	model = joblib.load(config.MODELS_DIR/model_name)
	
	return model