import pytest
import requests
from fetch_api_data import fetch_and_save_json

API_URL = "https://api.nationalize.io/?name=nathaniel"  # Sample API

def test_api_response():
    """Test if API returns a valid response."""
    response = requests.get(API_URL)
    assert response.status_code == 200, "API response code is not 200"
    assert response.headers["Content-Type"].startswith("application/json"), "Response is not JSON"
    assert len(response.json()) > 0, "API returned empty data"

def test_json_saving():
    """Test if fetch_and_save_json correctly saves the JSON data."""
    data = fetch_and_save_json(API_URL, "test_output.json")
    assert data is not None, "Function returned None"
    assert isinstance(data, list), "API response is not a list"
    assert len(data) > 0, "Saved JSON is empty"

if __name__ == "__main__":
    pytest.main()