from unittest.mock import Mock

def fetch_data(api_client):
    return api_client.get("/data")

def test_fetch_data():
    mock_client = Mock()
    mock_client.get.return_value = {"id": 1, "name": "Test"}
    result = fetch_data(mock_client)
    assert result == {"id": 1, "name": "Test"}