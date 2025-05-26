import requests
import pytest
import uuid

BASE_URL = "https://to-barrel-monitor.azurewebsites.net/barrels"

def test_vytvoreni_a_ziskani_barelu():
    # 1. Příprava vstupních dat
    test_id = str(uuid.uuid4())  # Unikátní ID pro každý test
    payload = {
        "id": test_id,
        "qr": "TestQR",
        "rfid": "TestRFID",
        "nfc": "TestNFC"
    }

    headers = {
        "Content-Type": "application/json"
    }

    # 2. Vytvoření nového barelu (POST)
    post_response = requests.post(BASE_URL, json=payload, headers=headers)
    print(f"[POST] Status: {post_response.status_code}")
    assert post_response.status_code == 201, f"POST selhal: {post_response.status_code}"
    print("[POST] Odpověď:", post_response.json())

    # 3. Získání stejného barelu (GET)
    get_url = f"{BASE_URL}/{test_id}"
    get_response = requests.get(get_url)
    print(f"[GET] Status: {get_response.status_code}")
    assert get_response.status_code == 200, f"GET selhal: {get_response.status_code}"
    
    response_data = get_response.json()
    print("[GET] Odpověď:", response_data)

    # 4. Porovnání dat
    assert response_data["id"] == payload["id"], "ID nesouhlasí"
    assert response_data["qr"] == payload["qr"], "QR nesouhlasí"
    assert response_data["rfid"] == payload["rfid"], "RFID nesouhlasí"
    assert response_data["nfc"] == payload["nfc"], "NFC nesouhlasí"