from classification_model.processors.validation import validate_inputs
from classification_model.config import config

def test_validation(raw_data):
    validated_data ,errors = validate_inputs(input_data=raw_data[config.SELECTED_FEATURES])

    assert len(validated_data) == len(raw_data) - 1

def test_validate_inputs_identifies_errors(raw_data):
    # Given
    test_inputs = raw_data.copy()

    # introduce errors
    test_inputs.at[1, "LOCATION_ID"] = 50  

    # When
    validated_inputs, errors = validate_inputs(input_data=test_inputs[config.SELECTED_FEATURES])

    # Then
    assert errors
    assert errors[1] == {"LOCATION_ID": ["Not a valid string."]}