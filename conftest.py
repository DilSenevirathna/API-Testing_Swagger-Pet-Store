import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    return APIClient("https://petstore.swagger.io/v2")

@pytest.fixture
def pet_data():
    return {
        "id": 123456789,
        "category": {
            "id": 1,
            "name": "dog"
        },
        "name": "doggie_test",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 1,
                "name": "tag1"
            }
        ],
        "status": "available"
    }
