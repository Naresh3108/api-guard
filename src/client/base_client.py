# base_client.py
# our main API client - all tests use this

import httpx
from config.settings import settings

class APIClient:
    
    def __init__(self):
        self.base_url = settings.base_url
        self.timeout = settings.timeout
    
    def get(self, endpoint, headers=None):
        url = self.base_url + endpoint
        response = httpx.get(url, headers=headers, timeout=self.timeout)
        return response
    
    def post(self, endpoint, data, headers=None):
        url = self.base_url + endpoint
        response = httpx.post(url, json=data, headers=headers, timeout=self.timeout)
        return response
    
    def put(self, endpoint, data, headers=None):
        url = self.base_url + endpoint
        response = httpx.put(url, json=data, headers=headers, timeout=self.timeout)
        return response
    
    def delete(self, endpoint, headers=None):
        url = self.base_url + endpoint
        response = httpx.delete(url, headers=headers, timeout=self.timeout)
        return response

client = APIClient()