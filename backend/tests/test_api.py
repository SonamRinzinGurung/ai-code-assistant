from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_explain():
    response = client.post(
        "/api/explain", json={"code": "def add(a,b): return a+b"})
    assert response.status_code == 200
    assert "explanation" in response.json()
