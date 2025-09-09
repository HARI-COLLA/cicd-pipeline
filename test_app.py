# Simple test to verify the Flask app works
import app

def test_hello():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data
    print("Test passed!")