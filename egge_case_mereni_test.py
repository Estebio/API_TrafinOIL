import requests
import pytest
import uuid

BASE_URL = "https://to-barrel-monitor.azurewebsites.net"
MEASUREMENT_ENDPOINT = f"{BASE_URL}/measurements"

VALID_BARREL_ID = "3fa85f64-5717-4562-b3fc-2c963f66afa6"

def vytvoreni_mereni(payload):
    headers = {"Content-Type": "application/json"}
    return requests.post(MEASUREMENT_ENDPOINT, json=payload, headers=headers)

def test_post_missing_required_fields():
    # Chybí barrelId (povinné)
    payload = {
        "id": str(uuid.uuid4()),
        # "barrelId" chybí
        "dirtLevel": 10.0,
        "weight": 50.0
    }
    response = vytvoreni_merenit(payload)
    print(f"Missing barrelId status: {response.status_code}, odpověď: {response.text}")
    assert response.status_code in (400, 422), "API nevaliduje chybějící barrelId správně"

    # Chybí dirtLevel (povinné)
    payload = {
        "id": str(uuid.uuid4()),
        "barrelId": VALID_BARREL_ID,
        # "dirtLevel" chybí
        "weight": 50.0
    }
    response = pvytvoreni_mereni(payload)
    print(f"Missing dirtLevel status: {response.status_code}, odpověď: {response.text}")
    assert response.status_code in (400, 422), "API nevaliduje chybějící dirtLevel správně"

   

def test_post_invalid_field_types():
    # dirtLevel jako text místo čísla
    payload = {
        "id": str(uuid.uuid4()),
        "barrelId": VALID_BARREL_ID,
        "dirtLevel": "necislo",
        "weight": 50.0
    }
    response = post_measurement(payload)
    print(f"Invalid dirtLevel type status: {response.status_code}, odpověď: {response.text}")
    assert response.status_code in (400, 422), "API nevaliduje typ dirtLevel správně"

    # weight jako text místo čísla
    payload = {
        "id": str(uuid.uuid4()),
        "barrelId": VALID_BARREL_ID,
        "dirtLevel": 10.0,
        "weight": "necislo"
    }
    response = post_measurement(payload)
    print(f"Invalid weight type status: {response.status_code}, odpověď: {response.text}")
    assert response.status_code in (400, 422), "API nevaliduje typ weight správně"
