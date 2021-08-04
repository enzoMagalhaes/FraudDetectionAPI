from classification_model.config import config

def load_dataset(filename="audit_data.csv"):
	import pandas as pd
	df = pd.read_csv(config.DATASETS_DIR/filename)
	
	# rename the bad name
	df.rename(columns={"Score_B.1":"Score_B_1"}, inplace=True)

	return df 

def save_model(model,model_name=config.MODEL_NAME):
	import joblib

	joblib.dump(model,config.MODELS_DIR/model_name)

def load_model(model_name=config.MODEL_NAME):
	import joblib 
	model = joblib.load(config.MODELS_DIR/model_name)
	
	return model