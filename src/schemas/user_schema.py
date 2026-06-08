# user_schema.py
# this file describes what a user object should look like
# pydantic will check if the API response matches this structure

from pydantic import BaseModel

# this is what a single user looks like
class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

# this is what the API returns when we get one user
class SingleUserResponse(BaseModel):
    data: User

# this is what the API returns when we get a list of users
class UserListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[User]