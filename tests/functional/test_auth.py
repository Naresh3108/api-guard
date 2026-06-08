import pytest
import httpx

HEADERS = {"x-api-key": "free_user_3ErYOaVb2twqvhn0qK8F1ugBjn4"}
BASE = "https://reqres.in/api"

@pytest.mark.auth
def test_login_success():
    # login with correct credentials should return 200
    credentials = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = httpx.post(f"{BASE}/login", json=credentials, headers=HEADERS)
    assert response.status_code == 200

@pytest.mark.auth
def test_login_returns_token():
    # successful login should give us a token
    credentials = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = httpx.post(f"{BASE}/login", json=credentials, headers=HEADERS)
    data = response.json()
    assert "token" in data

@pytest.mark.auth
def test_login_wrong_password():
    # reqres.in accepts any password for existing users
    # so wrong password still returns 200 - this is expected behavior for this test API
    # in a real app this would return 401
    credentials = {"email": "eve.holt@reqres.in", "password": "wrongpassword"}
    response = httpx.post(f"{BASE}/login", json=credentials, headers=HEADERS)
    assert response.status_code == 200

@pytest.mark.auth
def test_login_missing_password():
    # missing password should return 400
    credentials = {"email": "eve.holt@reqres.in"}
    response = httpx.post(f"{BASE}/login", json=credentials, headers=HEADERS)
    assert response.status_code == 400

@pytest.mark.auth
def test_login_missing_email():
    # missing email should return 400
    credentials = {"password": "cityslicka"}
    response = httpx.post(f"{BASE}/login", json=credentials, headers=HEADERS)
    assert response.status_code == 400