import pytest
import httpx
import time

HEADERS = {"x-api-key": "free_user_3ErYOaVb2twqvhn0qK8F1ugBjn4"}
BASE = "https://reqres.in/api"

# how fast the API should respond (in seconds)
MAX_TIME = 3.0

@pytest.mark.performance
def test_get_users_response_time():
    # getting all users should be fast
    start = time.time()
    httpx.get(f"{BASE}/users?page=1", headers=HEADERS)
    end = time.time()
    assert (end - start) < MAX_TIME

@pytest.mark.performance
def test_get_single_user_response_time():
    # getting one user should be fast
    start = time.time()
    httpx.get(f"{BASE}/users/2", headers=HEADERS)
    end = time.time()
    assert (end - start) < MAX_TIME

@pytest.mark.performance
def test_create_user_response_time():
    # creating a user should be fast
    start = time.time()
    httpx.post(f"{BASE}/users", json={"name": "Naresh", "job": "SDET"}, headers=HEADERS)
    end = time.time()
    assert (end - start) < MAX_TIME

@pytest.mark.performance
def test_login_response_time():
    # login should be fast
    start = time.time()
    httpx.post(f"{BASE}/login", json={"email": "eve.holt@reqres.in", "password": "cityslicka"}, headers=HEADERS)
    end = time.time()
    assert (end - start) < MAX_TIME

@pytest.mark.performance
def test_delete_response_time():
    # delete should be fast
    start = time.time()
    httpx.delete(f"{BASE}/users/2", headers=HEADERS)
    end = time.time()
    assert (end - start) < MAX_TIME