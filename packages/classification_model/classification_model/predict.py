from classification_model.processors import data_management as dm 
from classification_model.config import config 
from classification_model.processors.validation import validate_inputs
from classification_model import __version__

import logging
_logger = logging.getLogger(__name__)

def make_prediction(X):
	import pandas as pd 
	X = pd.DataFrame(X)

	# catch error if input doesnt have all the selected features
	try:
		X = X[config.SELECTED_FEATURES]
	except Exception as errors:
		return {"prediction":None,"version":__version__,"errors":str(errors)}

	# LOCATION_ID feature in an str even though they are majoritarily numbers  
	if X["LOCATION_ID"].dtype == "int64":
		X["LOCATION_ID"] = X["LOCATION_ID"].apply(str)

	validated_inputs,errors = validate_inputs(input_data=X)

	if errors:
		return {"prediction":None,"version":__version__,"errors":errors}

	model = dm.load_model()

	prediction = model.predict(validated_inputs)

	_logger.info(
			f"Making predictions with model version: {__version__}"
			f"Predictions: {prediction}"
		)

	return {"prediction":prediction,"version":__version__,"errors":errors}