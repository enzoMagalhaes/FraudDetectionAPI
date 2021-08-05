import pytest
from classification_model.config import config 
from classification_model.processors import data_management as dm 

@pytest.fixture()
def pipeline_inputs():
	df = dm.load_dataset()
	from sklearn.model_selection import train_test_split
	xtrain,xtest,ytrain,ytest = train_test_split(df[config.SELECTED_FEATURES],df[config.TARGET]
												 ,test_size=0.2,random_state=0)

	return xtrain,xtest,ytrain,ytest

@pytest.fixture()
def raw_data():
	df = dm.load_dataset()
	return df


@pytest.fixture()
def json_sample():
	
	sample = open("tests/sample_input.json",)

	import json
	data = json.load(sample)

	sample.close()
	return data