from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_main_sequence():
    payload = {
        "temperature": 5778,
        "luminosity": 1.0,
        "radius": 1.0,
        "absolute_magnitude": 4.83,
        "spectral_class": "G"
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "predicted_type" in data
    assert "confidence" in data
    assert isinstance(data["confidence"], float)

def test_invalid_spectral_class():
    payload = {
        "temperature": 5000,
        "luminosity": 0.5,
        "radius": 0.9,
        "absolute_magnitude": 6.0,
        "spectral_class": "Z"  # invalid
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 422 # Unprocessable Entity
    
def test_missing_field():
    payload = {
        "temperature": 5000,
        "luminosity": 0.5,
        # "radius" is missing
        "absolute_magnitude": 6.0,
        "spectral_class": "K"
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 422

def test_valid_spectral_class():
    payload = {
        "temperature": 3000,
        "luminosity": 0.01,
        "radius": 0.1,
        "absolute_magnitude": 15.0,
        "spectral_class": "M"
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["predicted_type"] == "Red Dwarf"
    assert isinstance(data["confidence"], float)