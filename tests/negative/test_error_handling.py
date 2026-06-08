import pytest
import httpx

HEADERS = {"x-api-key": "free_user_3ErYOaVb2twqvhn0qK8F1ugBjn4"}
BASE = "https://reqres.in/api"

@pytest.mark.negative
def test_get_user_that_doesnt_exist():
    # user 9999 doesn't exist - should return 404
    response = httpx.get(f"{BASE}/users/9999", headers=HEADERS)
    assert response.status_code == 404

@pytest.mark.negative
def test_get_user_invalid_id():
    # letters instead of number - should return 404
    response = httpx.get(f"{BASE}/users/abc", headers=HEADERS)
    assert response.status_code == 404

@pytest.mark.negative
def test_create_user_empty_body():
    # sending empty data - API should still respond
    response = httpx.post(f"{BASE}/users", json={}, headers=HEADERS)
    assert response.status_code in [200, 201, 400]

@pytest.mark.negative
def test_login_empty_body():
    # sending no credentials at all
    response = httpx.post(f"{BASE}/login", json={}, headers=HEADERS)
    assert response.status_code == 400

@pytest.mark.negative
def test_login_invalid_email_format():
    # sending a badly formatted email
    credentials = {"email": "notanemail", "password": "test"}
    response = httpx.post(f"{BASE}/login", json=credentials, headers=HEADERS)
    assert response.status_code in [400, 200]

@pytest.mark.negative
def test_no_api_key():
    # calling without API key should return 401
    response = httpx.get(f"{BASE}/users")
    assert response.status_code == 401