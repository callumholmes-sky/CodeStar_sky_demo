import json
import pytest
from helloworld.application import application


@pytest.fixture
def client():
    return application.test_client()


def test_response(client):
    result = client.get()
    response_body = json.loads(result.get_data())
    assert result.status_code == 200
    assert result.headers['Content-Type'] == 'application/json'
    assert response_body['Output'] == 'Hello World'

def test_add_fail(client):
    result = client.get('/add/12/23.4')
    response_body = json.loads(result.get_data())
    assert result.status_code == 404

def test_add_success(client):
    result = client.get('/add/12.1/23.4')
    response_body = json.loads(result.get_data())
    assert result.status_code == 200
    assert result.headers['Content-Type'] == 'application/json'
    assert response_body['Output'] == 35.5


