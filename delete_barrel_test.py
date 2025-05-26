import requests
import pytest

BASE_URL = "https://to-barrel-monitor.azurewebsites.net/barrels"
TEST_BARREL_ID = "7e2c283a-05fa-494b-aa04-03a21bb6bdb9"

def test_delete_barrel():
    # Sestav URL pro DELETE požadavek
    delete_url = f"{BASE_URL}/{TEST_BARREL_ID}"
    
    # Odeslání DELETE požadavku
    response = requests.delete(delete_url)

    # Očekávaný stavový kód – např. 204 No Content nebo 200 OK
    assert response.status_code in [200, 204], f"Unexpected status code: {response.status_code}"
    
    # Případná kontrola, že tělo odpovědi je prázdné
    if response.status_code == 204:
        assert response.text == '', "Expected empty response for 204 No Content"