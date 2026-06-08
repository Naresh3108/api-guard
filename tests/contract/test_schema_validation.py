import pytest
import httpx
from pydantic import BaseModel

HEADERS = {"x-api-key": "free_user_3ErYOaVb2twqvhn0qK8F1ugBjn4"}
BASE = "https://reqres.in/api"

# this is what a single user should look like
class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

# this is what the full response should look like
class UserListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[User]

# this is what a single user response looks like
class SingleUserResponse(BaseModel):
    data: User

@pytest.mark.contract
def test_user_list_schema():
    # check the entire response matches our expected structure
    response = httpx.get(f"{BASE}/users?page=1", headers=HEADERS)
    data = response.json()
    # pydantic will raise an error if structure doesn't match
    validated = UserListResponse(**data)
    assert validated.page == 1

@pytest.mark.contract
def test_single_user_schema():
    # check a single user response matches our schema
    response = httpx.get(f"{BASE}/users/2", headers=HEADERS)
    data = response.json()
    validated = SingleUserResponse(**data)
    assert validated.data.id == 2

@pytest.mark.contract
def test_user_email_is_string():
    # make sure email is always a string
    response = httpx.get(f"{BASE}/users/2", headers=HEADERS)
    data = response.json()
    validated = SingleUserResponse(**data)
    assert isinstance(validated.data.email, str)

@pytest.mark.contract
def test_user_id_is_integer():
    # make sure id is always an integer not a string
    response = httpx.get(f"{BASE}/users/2", headers=HEADERS)
    data = response.json()
    validated = SingleUserResponse(**data)
    assert isinstance(validated.data.id, int)

@pytest.mark.contract
def test_user_list_has_correct_fields():
    # check all required fields exist in every user
    response = httpx.get(f"{BASE}/users?page=1", headers=HEADERS)
    data = response.json()
    validated = UserListResponse(**data)
    for user in validated.data:
        assert user.id is not None
        assert user.email is not None
        assert user.first_name is not None