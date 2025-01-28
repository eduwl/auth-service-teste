import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI, HTTPException
from unittest.mock import Mock

from src.controller.login import LoginController
from src.domain import UseCase, UserNotFound

@pytest.fixture
def mock_usecase():
    return Mock(spec=UseCase)

@pytest.fixture
def app(mock_usecase):
    controller = LoginController(usecase=mock_usecase)
    app = FastAPI()
    app.include_router(controller.router)
    return app

def test_login_success(app, mock_usecase):
    mock_usecase.execute.return_value = "mocked_token"
    
    client = TestClient(app)
    payload = {"username": "eduwl", "password": "testpass"}
    response = client.post("/fake/token", json=payload)

    assert(response.status_code == 200)
    assert(response.json() == {"token": "mocked_token"})

def test_login_missing_data(app, mock_usecase):
    mock_usecase.execute.side_effect = None
    
    client = TestClient(app)
    payload = {"username": "", "password": "testpass"}
    response = client.post("/fake/token", json=payload)

    assert(response.status_code == 400)
    assert(response.json() == {"detail": "Missing login information"})

def test_login_user_not_found(app, mock_usecase):
    mock_usecase.execute.side_effect = UserNotFound("User not found")
    
    client = TestClient(app)
    payload = {"username": "eduwl", "password": "testpass"}
    response = client.post("/fake/token", json=payload)

    assert(response.status_code == 401)
    assert(response.json() == {"detail": "Unauthorized"})

def test_login_invalid_payload(app):
    client = TestClient(app)
    invalid_payload = {"username": "testuser"}

    response = client.post("/fake/token", json=invalid_payload)

    assert(response.status_code == 422)
    assert(response.json()["detail"][0]["loc"] == ["body", "password"])