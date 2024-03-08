from fastapi.testclient import TestClient
import json
from ..main import app
import os
import sys



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
client = TestClient(app)


def test_get_ip_info_task():
    response_task = client.get(
        "/api/v1/tasks?ip=5.179.3.4"
    )
    assert response_task.status_code == 201
    assert "task_id" in response_task.json()

   


def test_get_status():
    response_task = client.get(
        "/api/v1/tasks?ip=5.179.3.4"
    )
    assert response_task.status_code == 201
    assert "task_id" in response_task.json()
    response_status = client.get(
       f"/api/v1/tasks/status/{response_task.json()['task_id']}"
    )
    assert response_status.status_code == 200
    assert "task_id" in response_status.json()
    assert "task_status" in response_status.json()
    assert "task_result" in response_status.json()