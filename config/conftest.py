# conftest.py
# this file is special in pytest
# fixtures defined here are available to ALL tests automatically
# think of fixtures as "setup" code that runs before a test

import pytest
from src.client.base_client import APIClient

# this fixture creates a fresh API client for each test
@pytest.fixture
def api_client():
    # create a new client
    client = APIClient()
    # give it to the test
    return client

# this fixture gives tests a valid user ID to work with
@pytest.fixture
def valid_user_id():
    return 2

# this fixture gives tests a user that doesn't exist
@pytest.fixture
def invalid_user_id():
    return 9999