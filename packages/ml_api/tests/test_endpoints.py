import json
import time

import numpy as np
import pytest

from classification_model.processors.data_management import load_dataset


@pytest.mark.integration
def test_health_endpoint(client):
    # When
    response = client.get("/")

    # Then
    assert response.status_code == 200
    assert json.loads(response.data) == {"status": "OK"}


def test_prediction_endpoint(client):
    # Given
    test_inputs_df = load_dataset()  # dataframe

    # When
    response = client.post("/predict", json=test_inputs_df.to_dict(orient="records"))
    
    # Then
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["errors"] is None
    assert len(data["predictions"]) == len(test_inputs_df) - 1 # -1 because the validation filters one row
    assert isinstance(data["predictions"][0],int)


def test_json_input(client,json_sample):

    response = client.post("/predict", json=json_sample)

    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["errors"] is None
    assert isinstance(data["predictions"][0],int)


