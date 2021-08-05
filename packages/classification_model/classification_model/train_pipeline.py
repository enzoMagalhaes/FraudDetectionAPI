from classification_model.processors import data_management as dm
from classification_model.config import config 
from classification_model.pipeline import pipeline
from classification_model.processors.validation import validate_inputs

import logging
_logger = logging.getLogger(__name__)

def train_pipeline():
	df = dm.load_dataset()

	#Drop the NA row 
	df.drop(index=config.NA_INDEX,inplace=True)

	df,errors = validate_inputs(input_data=df)

	from sklearn.model_selection import train_test_split
	xtrain,xtest,ytrain,ytest = train_test_split(df[config.SELECTED_FEATURES],df[config.TARGET]
												,test_size=0.2,random_state=0)

	pipeline.fit(xtrain,ytrain)

	dm.save_model(pipeline)
	_logger.warning("model saved successfully!")

if __name__ == "__main__":
	train_pipeline()