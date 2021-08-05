from classification_model.processors import data_management as dm 
from classification_model.config import config 
from classification_model.processors.validation import validate_inputs

import logging
_logger = logging.getLogger(__name__)

def make_prediction(X):
	import pandas as pd 
	X = pd.DataFrame(X[config.SELECTED_FEATURES])

	validated_inputs,errors = validate_inputs(input_data=X)

	if errors:
		return {"prediction":None,"version":__version__,"errors":errors}

	model = dm.load_model()

	prediction = model.predict(validated_inputs)

	from classification_model import __version__
	_logger.info(
			f"Making predictions with model version: {__version__}"
			f"Predictions: {prediction}"
		)

	from classification_model import __version__
	return {"prediction":prediction,"version":__version__,"errors":errors}