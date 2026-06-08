# API Guard 🛡️

API Test Automation Framework built with Python, pytest, httpx, Pydantic v2, and Allure.

## Tech Stack
- Python 3.14
- pytest
- httpx
- Pydantic v2
- Allure Reports
- GitHub Actions (coming soon)

## Test Coverage
- 36 automated tests
- Smoke, Functional, Auth, Contract, Negative, Performance

## How to Run

### Install dependencies
pip install -r requirements.txt

### Run all tests
pytest -v

### Run by category
pytest -m smoke -v
pytest -m regression -v
pytest -m contract -v
pytest -m negative -v
pytest -m performance -v

### Generate Allure Report
pytest -v --alluredir=reports/allure-results
allure serve reports/allure-results

## Project Structure
- config/ - settings and fixtures
- src/ - API client and schemas
- tests/ - all test files
- testdata/ - test data files