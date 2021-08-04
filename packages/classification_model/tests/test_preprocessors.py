from classification_model.processors import preprocessors as p
from classification_model.config import config 

def test_RareLabelEncoder(pipeline_inputs):
	xtrain,xtest,ytrain,ytest = pipeline_inputs

	imputer = p.RareLabelEncoder(config.CATEGORICAL_FEATURE,0.5)

	transformed_data = imputer.fit_transform(xtest)	

	counter = 0

	feature = config.CATEGORICAL_FEATURE

	if(len(xtest[feature].value_counts().index) > 
		len(transformed_data[feature].value_counts().index)):
		counter += 1

	assert counter > 0


def test_CategoricalEncoder(pipeline_inputs):
	xtrain,xtest,ytrain,ytest = pipeline_inputs

	imputer = p.CategoricalEncoder(config.CATEGORICAL_FEATURE)

	transformed_data = imputer.fit_transform(xtest)

	assert xtest[config.CATEGORICAL_FEATURE].dtype == "object"
	assert transformed_data[config.CATEGORICAL_FEATURE].dtype == "int64"