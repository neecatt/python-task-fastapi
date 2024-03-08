from fastapi.testclient import TestClient
import json
from faker import Faker
from ..main import app
import os
import sys



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
client = TestClient(app)
fake = Faker()

def test_get_current_user():
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
    response = client.get(
        "/api/v1/users/",
        headers={"Authorization": f"Bearer {response.json()['access_token']}"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == username



    