import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

TEST_HEADERS = {"X-User-Id": "test_user"}

def test_generate_rtc_token():
    response = client.post(
        "/api/tokens/rtc",
        headers=TEST_HEADERS,
        json={"channel": "test_channel", "uid": "123", "role": "host"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    assert data["expires_in"] == 3600
    assert data["token"].startswith("0069714")

def test_generate_rtm_token():
    response = client.post(
        "/api/tokens/rtm",
        headers=TEST_HEADERS,
        json={"uid": "123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    assert data["token"].startswith("0069714")