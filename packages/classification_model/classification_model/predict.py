from classification_model.processors import data_management as dm 
from classification_model.config import config 
from classification_model.processors.validation import validate_inputs


def make_prediction(X):
	import pandas as pd 
	X = pd.DataFrame(X[config.SELECTED_FEATURES])

	validated_inputs,errors = validate_inputs(input_data=X)

	model = dm.load_model()

	prediction = model.predict(validated_inputs)

	from classification_model import __version__

	return {"prediction":prediction,"version":__version__,"errors":errors}