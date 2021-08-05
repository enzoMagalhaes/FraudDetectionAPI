import pytest
from api.app import create_app


@pytest.fixture(scope='session')
def app():
    app = create_app()
    with app.app_context():
        yield app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client  # Has to be yielded to access session cookies

@pytest.fixture()
def json_sample():
    
    sample = open("tests/sample_input.json",)

    import json
    data = json.load(sample)

    sample.close()
    return data