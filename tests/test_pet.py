import pytest

class TestPet:
    def test_create_pet(self, api_client, pet_data):
        response = api_client.post("pet", pet_data)
        assert response.status_code == 200
        assert response.json()["name"] == pet_data["name"]
        assert response.json()["id"] == pet_data["id"]

    def test_get_pet(self, api_client, pet_data):
        # Ensure pet exists first
        api_client.post("pet", pet_data)
        
        response = api_client.get(f"pet/{pet_data['id']}")
        assert response.status_code == 200
        assert response.json()["id"] == pet_data["id"]

    def test_update_pet(self, api_client, pet_data):
        # Ensure pet exists first
        api_client.post("pet", pet_data)
        
        pet_data["name"] = "doggie_updated"
        response = api_client.put("pet", pet_data)
        assert response.status_code == 200
        assert response.json()["name"] == "doggie_updated"

    def test_delete_pet(self, api_client, pet_data):
        # Ensure pet exists first
        api_client.post("pet", pet_data)
        
        response = api_client.delete(f"pet/{pet_data['id']}")
        assert response.status_code == 200
        
        # Verify deletion
        get_response = api_client.get(f"pet/{pet_data['id']}")
        assert get_response.status_code == 404
