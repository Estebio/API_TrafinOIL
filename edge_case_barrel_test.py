import requests
import pytest
import uuid

BASE_URL = "https://to-barrel-monitor.azurewebsites.net"
BARREL_ENDPOINT = f"{BASE_URL}/barrels"

def post_barrel(payload):
    headers = {"Content-Type": "application/json"}
    return requests.post(BARREL_ENDPOINT, json=payload, headers=headers)

def test_valid_minimal_barrel():
    """Validní barel s minimální délkou hodnot (1 znak)."""
    payload = {
        "id": str(uuid.uuid4()),
        "qr": "A",
        "rfid": "B",
        "nfc": "C"
    }
    response = post_barrel(payload)
    print("Valid minimal payload:", response.status_code, response.text)
    assert response.status_code == 201

def test_empty_qr_should_fail():
    """Prázdný QR – porušení minLength: 1"""
    payload = {
        "id": str(uuid.uuid4()),
        "qr": "",
        "rfid": "valid",
        "nfc": "valid"
    }
    response = post_barrel(payload)
    print("Empty QR:", response.status_code, response.text)
    assert response.status_code in (400, 422)

def test_empty_rfid_should_fail():
    """Prázdný RFID – porušení minLength: 1"""
    payload = {
        "id": str(uuid.uuid4()),
        "qr": "valid",
        "rfid": "",
        "nfc": "valid"
    }
    response = post_barrel(payload)
    print("Empty RFID:", response.status_code, response.text)
    assert response.status_code in (400, 422)

def test_empty_nfc_should_fail():
    """Prázdný NFC – porušení minLength: 1"""
    payload = {
        "id": str(uuid.uuid4()),
        "qr": "valid",
        "rfid": "valid",
        "nfc": ""
    }
    response = post_barrel(payload)
    print("Empty NFC:", response.status_code, response.text)
    assert response.status_code in (400, 422)

def test_missing_required_fields():
    """Chybějící všechna povinná pole"""
    payload = {
        "id": str(uuid.uuid4())
    }
    response = post_barrel(payload)
    print("Missing all required fields:", response.status_code, response.text)
    assert response.status_code in (400, 422)
