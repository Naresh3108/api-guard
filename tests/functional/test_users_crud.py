import pytest
import httpx

HEADERS = {"x-api-key": "free_user_3ErYOaVb2twqvhn0qK8F1ugBjn4"}
BASE = "https://reqres.in/api"

# ── GET ALL USERS ──────────────────────────────────────────
@pytest.mark.regression
def test_get_all_users():
    # check we can get a list of users
    response = httpx.get(f"{BASE}/users?page=1", headers=HEADERS)
    assert response.status_code == 200

@pytest.mark.regression
def test_get_all_users_has_data():
    # check the list actually has users in it
    response = httpx.get(f"{BASE}/users?page=1", headers=HEADERS)
    data = response.json()
    assert len(data["data"]) > 0

@pytest.mark.regression
def test_get_all_users_has_pagination():
    # check pagination fields exist
    response = httpx.get(f"{BASE}/users?page=1", headers=HEADERS)
    data = response.json()
    assert "page" in data
    assert "total" in data
    assert "total_pages" in data

# ── GET SINGLE USER ────────────────────────────────────────
@pytest.mark.regression
def test_get_single_user():
    # get user with ID 2
    response = httpx.get(f"{BASE}/users/2", headers=HEADERS)
    assert response.status_code == 200

@pytest.mark.regression
def test_get_single_user_has_correct_id():
    # make sure the user returned is actually user 2
    response = httpx.get(f"{BASE}/users/2", headers=HEADERS)
    data = response.json()
    assert data["data"]["id"] == 2

@pytest.mark.regression
def test_get_single_user_has_email():
    # check user has an email field
    response = httpx.get(f"{BASE}/users/2", headers=HEADERS)
    data = response.json()
    assert "email" in data["data"]

# ── CREATE USER ────────────────────────────────────────────
@pytest.mark.regression
def test_create_user():
    # create a new user
    new_user = {"name": "Naresh", "job": "SDET"}
    response = httpx.post(f"{BASE}/users", json=new_user, headers=HEADERS)
    assert response.status_code == 201

@pytest.mark.regression
def test_create_user_returns_id():
    # check the created user gets an ID back
    new_user = {"name": "Naresh", "job": "SDET"}
    response = httpx.post(f"{BASE}/users", json=new_user, headers=HEADERS)
    data = response.json()
    assert "id" in data

@pytest.mark.regression
def test_create_user_returns_correct_name():
    # check the name we sent is in the response
    new_user = {"name": "Naresh", "job": "SDET"}
    response = httpx.post(f"{BASE}/users", json=new_user, headers=HEADERS)
    data = response.json()
    assert data["name"] == "Naresh"

# ── UPDATE USER ────────────────────────────────────────────
@pytest.mark.regression
def test_update_user():
    # update user 2 with a new job title
    updated_data = {"name": "Naresh", "job": "Senior SDET"}
    response = httpx.put(f"{BASE}/users/2", json=updated_data, headers=HEADERS)
    assert response.status_code == 200

@pytest.mark.regression
def test_update_user_returns_new_job():
    # check the updated job is in the response
    updated_data = {"name": "Naresh", "job": "Senior SDET"}
    response = httpx.put(f"{BASE}/users/2", json=updated_data, headers=HEADERS)
    data = response.json()
    assert data["job"] == "Senior SDET"

# ── DELETE USER ────────────────────────────────────────────
@pytest.mark.regression
def test_delete_user():
    # delete user 2 - should return 204 no content
    response = httpx.delete(f"{BASE}/users/2", headers=HEADERS)
    assert response.status_code == 204