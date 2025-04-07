import pytest
from app import app  # Import the Flask app instance

@pytest.fixture
def client():
    app.config['TESTING'] = True  # Enable testing mode
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')  # Simulate a GET request to the homepage
    assert response.status_code == 200  # Check if the response status code is 200
    assert b"Welcome" in response.data  # Check if "Welcome" is in the response data