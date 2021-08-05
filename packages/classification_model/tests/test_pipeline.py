from classification_model.processors import data_management as dm 
from classification_model.predict import make_prediction

def test_prediction(pipeline_inputs):
	xtrain,xtest,ytrain,ytest = pipeline_inputs

	result = make_prediction(xtest)

	assert len(result["prediction"]) == len(ytest)
	
	from sklearn.metrics import accuracy_score
	assert accuracy_score(ytest,result["prediction"]) == 1.0

def test_single_input_prediction(pipeline_inputs):
	xtrain,xtest,ytrain,ytest = pipeline_inputs

	result = make_prediction(xtest.iloc[0:1])


	assert result["prediction"][0]
