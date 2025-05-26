import requests
import uuid

BASE_URL = "https://to-barrel-monitor.azurewebsites.net"
BARREL_ENDPOINT = f"{BASE_URL}/barrels"
MEASUREMENT_ENDPOINT = f"{BASE_URL}/measurements"

NON_EXISTENT_ID = str(uuid.uuid4())

def test_get_nonexistent_barrel():
    """GET /barrels/{id} s neexistujícím UUID"""
    url = f"{BARREL_ENDPOINT}/{NON_EXISTENT_ID}"
    response = requests.get(url)
    print(f"GET non-existent barrel [{NON_EXISTENT_ID}]:", response.status_code, response.text)
    assert response.status_code == 404, "Měl být vrácen status 404 pro neexistující barrel"

def test_delete_nonexistent_barrel():
    """DELETE /barrels/{id} s neexistujícím UUID"""
    url = f"{BARREL_ENDPOINT}/{NON_EXISTENT_ID}"
    response = requests.delete(url)
    print(f"DELETE non-existent barrel [{NON_EXISTENT_ID}]:", response.status_code, response.text)
    assert response.status_code in (404, 204), "Očekáváme 404 pro neexistující barrel"

def test_get_nonexistent_measurement():
    """GET /measurements/{id} s neexistujícím UUID (pokud endpoint existuje)"""
    url = f"{MEASUREMENT_ENDPOINT}/{NON_EXISTENT_ID}"
    response = requests.get(url)
    print(f"GET non-existent measurement [{NON_EXISTENT_ID}]:", response.status_code, response.text)
    assert response.status_code == 404, "Očekáváme 404 pro neexistující měření"
