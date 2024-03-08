from fastapi.testclient import TestClient
import json
from faker import Faker
from ..main import app
import os
import sys



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
client = TestClient(app)
fake = Faker()

def test_signup():
    username = fake.user_name()
    password = fake.password()
    created_at = "string"
    response = client.post(
        "/api/v1/auth/signup",
        json={"username": username, "password": password, "created_at": created_at}
    )
    assert response.status_code == 201
    assert response.json()["user"]["username"] == username
    assert response.json()["message"] == "User created successfully"

def test_login():
    username = fake.user_name()
    password = fake.password()
    response = client.post(
        "/api/v1/auth/signup",
        json={"username": username, "password": password, "created_at": "string"}
    )
    assert response.status_code == 201
    response = client.post(
        "/api/v1/auth",
        data={"username": username, "password": password}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()

def test_refresh_access_token():
    username = fake.user_name()
    password = fake.password()
    response = client.post(
        "/api/v1/auth/signup",
        json={"username": username, "password": password, "created_at": "string"}
    )
    assert response.status_code == 201
    response = client.post(
        "/api/v1/auth",
        data={"username": username, "password": password}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()
    response = client.post(
        "/api/v1/auth/refresh",
        headers={"Authorization": f"Bearer {response.json()['refresh_token']}"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()