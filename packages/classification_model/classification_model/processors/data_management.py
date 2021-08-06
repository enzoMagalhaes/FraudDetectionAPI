from classification_model.config import config
from classification_model import __version__

import logging
_logger = logging.getLogger(__name__)

def load_dataset(filename="audit_data.csv"):
	import pandas as pd
	df = pd.read_csv(config.DATASETS_DIR/filename)
	df = df.drop(["Score_B.1"],axis=1)

	return df 

def save_model(model,model_name=f"{config.MODEL_NAME}_{__version__}.pkl"):
	import joblib

	joblib.dump(model,config.MODELS_DIR/model_name)
	_logger.info(f"saved model: {model_name}")

def load_model(model_name=f"{config.MODEL_NAME}_{__version__}.pkl"):
	import joblib 
	model = joblib.load(config.MODELS_DIR/model_name)
	
	return model