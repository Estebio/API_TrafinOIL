import requests
import pytest
import uuid

BASE_URL = "https://to-barrel-monitor.azurewebsites.net"
MEASUREMENT_ENDPOINT = f"{BASE_URL}/measurements"

def test_post_nove_mereni():
    measurement_id = str(uuid.uuid4())
    barrel_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"

    payload = {
        "id": measurement_id,
        "barrelId": barrel_id,
        "dirtLevel": 25.4,
        "weight": 90.7
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(MEASUREMENT_ENDPOINT, json=payload, headers=headers)
    print(f"Status kód: {response.status_code}")
    print("Odpověď:", response.text)

    assert response.status_code == 201, f"Očekáván kód 201, ale byl {response.status_code}"

    # Porovnání dat - vypíše pokud nesouhlasí data
    response_data = response.json()
    assert response_data["id"] == measurement_id, "ID měření nesouhlasí"
    assert response_data["barrelId"] == barrel_id, "barrelId nesouhlasí"
    assert response_data["dirtLevel"] == 25.4, "dirtLevel nesouhlasí"
    assert response_data["weight"] == 90.7, "weight nesouhlasí"
