# =============================================================================
# Modules
# =============================================================================

# Third-party
import pytest
from flask import Flask

# Testing
from routes import init_routes

# =============================================================================
# Tests
# =============================================================================

@pytest.fixture
def client():
    """
    Pytest fixture to create a test client for the Flask application
    
    Yields:
        FlaskClient: A test client to simulate HTTP requests
    """
    app = Flask(__name__)
    app.config["TESTING"] = True
    init_routes(app)
    
    with app.test_client() as client:
        yield client

def test_home(client):
    """
    Test if the home page loads successfully
    """
    response = client.get("/")
    print(response.data)
    assert response.status_code == 200
    assert b"Weather Data API" in response.data  # Check if page contains title

def test_get_temperature_valid(client):
    """
    Test fetching temperature data for a valid station and date
    """
    response = client.get("/api/v1/10/1988-10-25")
    assert response.status_code == 200
    json_data = response.get_json()
    assert "station" in json_data
    assert "date" in json_data
    assert "temperature" in json_data

def test_get_temperature_invalid(client):
    """
    Test error handling for an invalid station or date
    """
    response = client.get("/api/v1/9999/3000-01-01")
    assert response.status_code == 500  # Expecting failure for invalid data
    json_data = response.get_json()
    assert "error" in json_data

def test_all_data_valid(client):
    """
    Test retrieving all data for a valid station
    """
    response = client.get("/api/v1/10")
    assert response.status_code == 200
    json_data = response.get_json()
    assert isinstance(json_data, list)  # Should return a list of records

def test_all_data_invalid(client):
    """
    Test handling of an invalid station request
    """
    response = client.get("/api/v1/9999")
    assert response.status_code == 500
    json_data = response.get_json()
    assert "error" in json_data

def test_yearly_station_data_valid(client):
    """
    Test retrieving yearly data for a valid station and year
    """
    response = client.get("/api/v1/yearly/10/1988")
    assert response.status_code == 200
    json_data = response.get_json()
    assert isinstance(json_data, list)  # Expecting a list of data

def test_yearly_station_data_invalid(client):
    """
    Test handling of an invalid station or year request
    """
    response = client.get("/api/v1/yearly/9999/3000")
    assert response.status_code == 500
    json_data = response.get_json()
    assert "error" in json_data
