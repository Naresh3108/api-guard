# settings.py
# this file stores all the configuration for our project
# like the base URL of the API we are testing

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # base URL of the API we are testing
    base_url: str = "https://reqres.in/api"
    
    # how long to wait for a response (in seconds)
    timeout: int = 10
    
    # which environment we are running in
    environment: str = "dev"

# create one settings object to use everywhere
settings = Settings()