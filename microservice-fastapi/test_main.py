"""tests fastapi main.py using pytest"""

import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Coursera"}

#@app.get("/add/{num1}/{num2}")
def test_add(client):
    response = client.get("/add/1/2")
    assert response.status_code == 200
    assert response.json() == {"result": 3}

def test_subtract(client):
    response = client.get("/subtract/1/2")
    assert response.status_code == 200
    assert response.json() == {"result": -1}

def test_multiply(client):
    response = client.get("/multiply/1/2")
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_divide(client):
    response = client.get("/divide/1/2")
    assert response.status_code == 200
    assert response.json() == {"result": 0.5}
