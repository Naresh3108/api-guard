import pytest
import time
import httpx

KEY = "free_user_3ErYOaVb2twqvhn0qK8F1ugBjn4"
HEADERS = {"x-api-key": KEY}
URL = "https://reqres.in/api/users?page=1"

@pytest.mark.smoke
def test_api_is_alive():
    response = httpx.get(URL, headers=HEADERS)
    assert response.status_code == 200

@pytest.mark.smoke
def test_api_returns_json():
    response = httpx.get(URL, headers=HEADERS)
    data = response.json()
    assert "data" in data

@pytest.mark.smoke
def test_api_response_is_fast():
    start = time.time()
    httpx.get(URL, headers=HEADERS)
    end = time.time()
    assert (end - start) < 3