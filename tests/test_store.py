import pytest

class TestStore:
    def test_place_order(self, api_client):
        order_data = {
            "id": 1,
            "petId": 123456789,
            "quantity": 1,
            "shipDate": "2024-12-01T00:00:00.000+0000",
            "status": "placed",
            "complete": True
        }
        response = api_client.post("store/order", order_data)
        assert response.status_code == 200
        assert response.json()["status"] == "placed"

    def test_get_order(self, api_client):
        # Ensure order exists (relying on previous test or creating new one)
        order_data = {
          "id": 1,
          "petId": 123456789,
          "quantity": 1,
          "shipDate": "2024-12-01T00:00:00.000+0000",
          "status": "placed",
          "complete": True
        }
        api_client.post("store/order", order_data)

        response = api_client.get("store/order/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1

    def test_get_inventory(self, api_client):
        response = api_client.get("store/inventory")
        assert response.status_code == 200
        assert isinstance(response.json(), dict)
