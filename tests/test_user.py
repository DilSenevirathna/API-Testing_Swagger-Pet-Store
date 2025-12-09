import pytest
from faker import Faker

fake = Faker()

class TestUser:
    def test_create_user(self, api_client):
        user_data = {
            "id": 101,
            "username": "testuser1",
            "firstName": "Test",
            "lastName": "User",
            "email": "test@example.com",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 0
        }
        response = api_client.post("user", user_data)
        assert response.status_code == 200

    def test_get_user(self, api_client):
        # Create user first to ensure existence
        user_data = {
            "id": 102,
            "username": "testuser2",
            "firstName": "Test",
            "lastName": "User",
            "email": "test2@example.com",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 0
        }
        api_client.post("user", user_data)

        response = api_client.get("user/testuser2")
        assert response.status_code == 200
        assert response.json()["username"] == "testuser2"

    def test_login(self, api_client):
        params = {
            "username": "testuser2",
            "password": "password123"
        }
        response = api_client.get("user/login", params=params)
        assert response.status_code == 200
        assert "logged in user session" in response.json()["message"]

    def test_logout(self, api_client):
        response = api_client.get("user/logout")
        assert response.status_code == 200
