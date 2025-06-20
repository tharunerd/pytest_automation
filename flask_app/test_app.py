import pytest
from flask_app.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Welcome to the simple web app!"

def test_add_valid(client):
    response = client.get("/add?a=10&b=20")
    assert response.status_code == 200
    assert response.get_json()["result"] == 30

def test_add_invalid(client):
    response = client.get("/add?a=abc&b=1")
    assert response.status_code == 400
    assert "error" in response.get_json()